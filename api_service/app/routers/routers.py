from fastapi import APIRouter

from models import ShortenRequest

api_router = APIRouter()

@api_router.post("/shorten-url")
def shorten_url(body: ShortenRequest):
    pass

@api_router.get("/test/{item}")
def test():
    pass