from ninja.errors import HttpError


class ForbiddenError(HttpError):
    def __init__(self, message: str | None = None) -> None:
        message = message if message is not None else "Forbidden"
        super().__init__(status_code=403, message=message)
