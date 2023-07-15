from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from .logger import log


async def exception_handler(_: Request, exc: Exception) -> JSONResponse:
    log.error("Internal server error", exc_info=exc)
    return JSONResponse(
        content={"detail": "Internal Server Error"},
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )


def register_exception_handlers(app: FastAPI) -> None:
    app.add_exception_handler(Exception, exception_handler)
