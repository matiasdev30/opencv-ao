from .config import router, templates
from fastapi import Request

@router.get("/login")
async def login(request: Request):
    return templates.TemplateResponse(name="login.html", request={"request" : request, "message" : "login page"})