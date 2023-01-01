from django.contrib import admin

from .models import PlannedTask, PlannedPeriod


@admin.register(PlannedTask)
class PlannedTaskAdmin(admin.ModelAdmin):
    list_display = ("uuid", "is_completed", "owner")


@admin.register(PlannedPeriod)
class PlannedPeriodAdmin(admin.ModelAdmin):
    list_display = ("uuid", "from_date", "to_date", "tasks_completed", "tasks_moved", "tasks_total", "period_type")
