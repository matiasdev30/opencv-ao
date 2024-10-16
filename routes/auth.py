from fastapi.responses import HTMLResponse, RedirectResponse
from .config import router, templates
from fastapi import Form, Request
import os


@router.get("/login", response_class=HTMLResponse)
async def read_user(request: Request):
    return templates.TemplateResponse("login.html", {"request" : request})

