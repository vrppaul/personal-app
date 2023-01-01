import datetime

from django.http import Http404
from ninja import Router
from ninja.pagination import paginate

from libs.schemas.errors import GenericApiError
from planner.models import PlannedPeriod, PlannedPeriodQueryset, PlannedPeriodType
from planner.schemas import PlannedPeriodDetailSchema, PlannedPeriodTypeSchema
from planner.services import period_services

periods_router = Router()


@periods_router.get("/", response=list[PlannedPeriodDetailSchema])
@paginate
def get_day_periods(request, from_date: datetime.date, to_date: datetime.date) -> PlannedPeriodQueryset:
    """
    Returns all the existing day periods, that are inside the provided range.
    """
    return period_services.get_day_periods_within_range(from_date, to_date)


@periods_router.get("/current", response={200: PlannedPeriodDetailSchema, 404: GenericApiError})
def get_current_period(request, period_type: int = PlannedPeriodType.DAY) -> PlannedPeriod:
    """
    Finds the period of given type, which is applicable for the current date.
    If the period type is day, will try to return the today's period,
    if week, period of current week will be returned etc.

    If period was not found, raises 404.
    """
    period = period_services.get_current_period_of_type(period_type)
    if period is None:
        raise Http404

    return period


@periods_router.get("/types", response=list[PlannedPeriodTypeSchema])
def get_period_types(request):
    """
    Returns all the PlannedPeriod types in a convenient object.
    """
    return period_services.get_period_types()
