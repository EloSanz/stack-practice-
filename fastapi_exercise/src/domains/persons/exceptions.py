from fastapi import Request
from fastapi.responses import JSONResponse

class PersonDomainException(Exception):
    def __init__(self, message: str, status_code: int = 400):
        super().__init__(message)
        self.message = message
        self.status_code = status_code

async def person_domain_exception_handler(request: Request, exc: Exception):
    # Retrieve the status_code if it exists on the custom exception, default to 400
    status_code = getattr(exc, "status_code", 400)
    message = getattr(exc, "message", str(exc))
    return JSONResponse(
        status_code=status_code,
        content={"detail": message}
    )
