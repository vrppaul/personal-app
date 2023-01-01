import datetime

from django.utils import timezone

from planner.models import PlannedPeriod, PlannedPeriodType, PlannedPeriodQueryset


def get_day_periods_within_range(from_date: datetime.date, to_date: datetime.date) -> PlannedPeriodQueryset:
    return PlannedPeriod.objects.filter(from_date__gte=from_date, to_date__lte=to_date).daily()


def get_current_period_of_type(period_type: int) -> PlannedPeriod:
    current_date = timezone.datetime.today()
    return PlannedPeriod.objects.filter(from_date__lte=current_date, to_date__gte=current_date, period_type=period_type).first()


def get_period_types() -> list[dict[str, int | str]]:
    return [
        {"id": period_id, "name": period_name}
        for period_id, period_name in PlannedPeriodType.choices
    ]
