from typing import Literal

from pydantic import AnyHttpUrl, BaseModel


class PingRequest(BaseModel):
    url: AnyHttpUrl


class PingResponse(BaseModel):
    response: str


class PingError(BaseModel):
    error: str


class InfoResponse(BaseModel):
    Receiver: Literal["Cisco is the best!"]
