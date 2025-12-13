from models.response_schema import ResponseModel, APIError
from fastapi.responses import JSONResponse
from fastapi import Request


async def api_error_handler(request: Request, exc: Exception):
    if isinstance(exc, APIError):
        return JSONResponse(
            status_code=exc.status_code,
            content=ResponseModel(
                status="error", data=None, message=exc.detail
            ).model_dump(),
        )
    # Optionally handle unexpected exceptions in the same format
    return JSONResponse(
        status_code=500,
        content=ResponseModel(
            status="error", data=None, message="Internal Server Error"
        ).model_dump(),
    )
