import abc

from django.db import models
from django.http import HttpRequest


class PermissionException(Exception):
    pass


class PermissionBase(abc.ABC):
    def __init__(self, request: HttpRequest) -> None:
        self.request = request

    def check(self, *args, **kwargs) -> None:
        pass


class ModelObjectPermissionBase(PermissionBase, abc.ABC):
    @abc.abstractmethod
    def check_object(self, model_object: models.Model, *args, **kwargs) -> None:
        pass
