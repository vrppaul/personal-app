from ninja import NinjaAPI

from planner.api import planner_router
from libs.api_renderers import ORJSONRenderer


api = NinjaAPI(csrf=True, renderer=ORJSONRenderer())

api.add_router("/planner", planner_router)
