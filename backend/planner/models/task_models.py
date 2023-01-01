import uuid

from django.db import models

from core.models import OwnershipModel


class PlannedTask(OwnershipModel):
    uuid = models.UUIDField(default=uuid.uuid4)

    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    times_moved = models.PositiveSmallIntegerField(default=0)

    planned_period = models.ForeignKey("planner.PlannedPeriod", null=True, blank=True, on_delete=models.CASCADE, related_name="planned_tasks")

    def __str__(self):
        return f"{self.__class__.__name__}: {self.uuid}"
