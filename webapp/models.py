from typing import Literal

from pydantic import BaseModel, HttpUrl


class PingRequest(BaseModel):
    url: HttpUrl


class PingResponse(BaseModel):
    response: str


class PingError(BaseModel):
    error: str


class InfoResponse(BaseModel):
    Receiver: Literal["Cisco is the best!"]
