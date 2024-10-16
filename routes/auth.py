from fastapi.responses import HTMLResponse, RedirectResponse
from .config import router, templates
from fastapi import Form, Request

@router.get("/login", response_class=HTMLResponse)
async def read_user(request: Request):
    return templates.TemplateResponse("login.html", {"request" : request})

@router.post("/home")
async def home(request: Request, email: str = Form(...)):
    return templates.TemplateResponse("home.html", {"request": request, "email" : email})
    #return {"message": "Bem-vindo à página inicial!"}