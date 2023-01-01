from functools import wraps

from django.http import HttpRequest
from ninja.types import TCallable

from libs.errors import ForbiddenError
from libs.permissions.base import ModelObjectPermissionBase, PermissionException


def check_object_permissions(*permission_classes: type[ModelObjectPermissionBase]):
    def wrapper(func: TCallable) -> TCallable:
        @wraps(func)
        def decorator(request: HttpRequest, *args, **kwargs):
            model_object = func(request, *args, **kwargs)

            try:
                for permission_class in permission_classes:
                    permission = permission_class(request)
                    permission.check_object(model_object)
            except PermissionException:
                raise ForbiddenError()

            return model_object

        return decorator

    return wrapper
