from fastapi import Request
from fastapi.responses import HTMLResponse
from .config import router, templates

@router.get("/")
async def hello(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "message" : "Olá, Ninja templates com FastAPI"}) 


@router.get("/user/{username}", response_class=HTMLResponse)
async def read_user(request: Request, username: str):
    return templates.TemplateResponse("user.html", {"request" : request, "username": username})