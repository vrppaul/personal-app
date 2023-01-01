from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404
from ninja import Router
from ninja.pagination import paginate

from libs import crud
from libs.permissions.ownership import IsOwner
from libs.permissions.services import check_object_permissions
from libs.schemas.errors import GenericApiError
from planner.models import PlannedTask
from planner.schemas import PlannedTaskCreateSchema, PlannedTaskDetailSchema
from planner.services.task_services import get_user_tasks

tasks_router = Router()


@tasks_router.get("/", response={200: list[PlannedTaskDetailSchema]})
@paginate
def get_tasks(request) -> QuerySet[PlannedTask]:
    return get_user_tasks(request.user)


@tasks_router.post("/", response={201: PlannedTaskDetailSchema})
def create_task(request, task_params: PlannedTaskCreateSchema) -> PlannedTask:
    return crud.create(task_params, owner=request.user)


@tasks_router.get("/{uuid:task_uuid}", response={200: PlannedTaskDetailSchema, 403: GenericApiError, 404: GenericApiError})
@check_object_permissions(IsOwner)
def get_task_detail(request, task_uuid: str) -> PlannedTask:
    task = get_object_or_404(PlannedTask, uuid=task_uuid)

    return task


@tasks_router.get("/period/{uuid:period_uuid}", response={200: list[PlannedTaskDetailSchema]})
def get_period_tasks(request, period_uuid: str) -> QuerySet[PlannedTask]:
    """Returns all planned tasks owned by user created the request and which fall under the provided period.
    """
    return get_user_tasks(request.user, period_uuid)

