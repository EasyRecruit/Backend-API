from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import status


def success_response(message, data=None, code=status.HTTP_200_OK):
    payload = {
        'message': message,
        'data': data
    }
    payload = jsonable_encoder(payload)
    return JSONResponse(content=payload, status_code=code)

