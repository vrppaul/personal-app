from ninja import ModelSchema, Schema

from planner.models import PlannedPeriod


class PlannedPeriodDetailSchema(ModelSchema):
    class Config:
        model = PlannedPeriod
        model_fields = ("uuid", "from_date", "to_date", "tasks_completed", "tasks_moved", "tasks_total", "period_type")


class PlannedPeriodTypeSchema(Schema):
    id: int
    name: str
