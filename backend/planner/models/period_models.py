import uuid
from typing import Self

from django.db import models


class PlannedPeriodType(models.IntegerChoices):
    DAY = 1, "day"
    WEEK = 2, "week"
    MONTH = 3, "month"
    YEAR = 4, "year"


class PlannedPeriodQueryset(models.QuerySet):
    def daily(self) -> Self:
        return self.filter(period_type=PlannedPeriodType.DAY)


class PlannedPeriod(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4)

    from_date = models.DateField()
    to_date = models.DateField()

    tasks_completed = models.PositiveSmallIntegerField(default=0)
    tasks_moved = models.PositiveSmallIntegerField(default=0)
    tasks_total = models.PositiveSmallIntegerField(default=0)

    period_type = models.PositiveSmallIntegerField(choices=PlannedPeriodType.choices)

    # Custom manager
    objects = PlannedPeriodQueryset.as_manager()

    def __str__(self):
        return f"{self.from_date} - {self.to_date}: {self.get_period_type_display()}"
