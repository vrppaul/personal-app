from ninja import ModelSchema

from planner.models import PlannedTask


class PlannedTaskDetailSchema(ModelSchema):
    class Config:
        model = PlannedTask
        model_fields = ("uuid", "description", "is_completed", "times_moved", "planned_period")


class PlannedTaskCreateSchema(ModelSchema):
    class Config:
        model = PlannedTask
        model_fields = ("description",)
