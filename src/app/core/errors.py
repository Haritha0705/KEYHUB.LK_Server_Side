import logging

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

logger = logging.getLogger(__name__)


class APIError(Exception):
    """Application-level error carrying an HTTP status code and a message."""

    def __init__(self, code: int, message: str, error: dict | None = None):
        super().__init__(message)
        self.code = code
        self.message = message
        # Always a dict so callers can safely do `**e.error`.
        self.error = error or {}

    def __str__(self) -> str:
        return f"{self.code}: {self.message}"


class DBError(APIError):
    """Raised for database-layer failures."""
    pass


def register_exception_handlers(app: FastAPI) -> None:
    """Register app-wide exception handlers so routers stay free of try/except."""

    @app.exception_handler(APIError)
    async def handle_api_error(_: Request, exc: APIError) -> JSONResponse:
        return JSONResponse(
            status_code=exc.code,
            content={"message": exc.message, **exc.error},
        )

    @app.exception_handler(Exception)
    async def handle_unexpected_error(_: Request, exc: Exception) -> JSONResponse:
        logger.exception("Unhandled error: %s", exc)
        return JSONResponse(
            status_code=500,
            content={"message": "Internal Server Error"},
        )
