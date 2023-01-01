from django.db import models

from planner.models import PlannedTask
from users.models import User


def get_user_tasks(owner: User, period_uuid: str | None = None) -> models.QuerySet[PlannedTask]:
    return PlannedTask.objects.filter(owner=owner, planned_period__uuid=period_uuid)
