from http import HTTPStatus

from fastapi import FastAPI

from .models import InfoResponse, PingError, PingRequest, PingResponse

app = FastAPI()


@app.get("/info", response_model=InfoResponse, status_code=HTTPStatus.OK)
def info():
    return {"Receiver": "Cisco is the best!"}


@app.post(
    "/ping",
    response_model=PingResponse,
    status_code=HTTPStatus.OK,
    responses={HTTPStatus.BAD_REQUEST: {"model": PingError}},
)
async def ping(request: PingRequest):
    pass
