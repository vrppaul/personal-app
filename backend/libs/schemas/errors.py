from ninja import Schema


class GenericApiError(Schema):
    detail: str
