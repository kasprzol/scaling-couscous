import aiohttp
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

from .models import InfoResponse, PingError, PingRequest, PingResponse

app = FastAPI()


@app.get("/info", response_model=InfoResponse, status_code=status.HTTP_200_OK)
def info():
    """Simple hello message"""
    return InfoResponse(Receiver="Cisco is the best!")


@app.post(
    "/ping",
    response_model=PingResponse,
    status_code=status.HTTP_200_OK,
    responses={status.HTTP_400_BAD_REQUEST: {"model": PingError}},
)
async def ping(request: PingRequest):
    """Download and return the given url"""
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(request.url, ssl=False) as response:
                payload = await response.text()
                return PingResponse(response=payload)
    except Exception as e:
        error_msg = f"Error while retrieving the requested url: {e}"
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST, content={"error": error_msg}
        )
