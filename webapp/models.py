from typing import Literal

from pydantic import AnyHttpUrl, BaseModel


class PingRequest(BaseModel):
    """Model for the ping endpoint request body"""

    url: AnyHttpUrl


class PingResponse(BaseModel):
    """Model for the response of the ping endpoint"""

    response: str


class PingError(BaseModel):
    """Model for the error response of the ping endpoint"""

    error: str


class InfoResponse(BaseModel):
    """Model for the response of the info endpoint"""

    Receiver: Literal["Cisco is the best!"]
