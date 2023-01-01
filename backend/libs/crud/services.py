from typing import TypeVar

from django.db import models
from ninja import ModelSchema


TModel = TypeVar("TModel", bound=models.Model)


def create(params: ModelSchema, **additional_params) -> TModel:
    return params.Config.model.objects.create(**params.dict(), **additional_params)
