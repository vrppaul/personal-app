from ninja import Router
from ninja.security import django_auth

from .views import periods_router, tasks_router


planner_router = Router(auth=django_auth)

planner_router.add_router("/tasks", tasks_router)
planner_router.add_router("/periods", periods_router)
