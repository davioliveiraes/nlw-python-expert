from src.views.http_types.http_response import HttpResponse
from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError

def handler_errors(error: Exception) -> HttpResponse:
    if isinstance(error, HttpUnprocessableEntityError):
        # enviar para um log
        # enviar para um email de notificação
        return HttpResponse(
            status_code=error.status_code,
            body={
                "errors": [{
                    "title": error.name,
                    "detail": error.message
                }]
            }
        )


    return HttpResponse(
        status_code=500,
        body={
            "errors": [{
                "title": "Server Error",
                "detail": str(error)
            }]
        }
    )
