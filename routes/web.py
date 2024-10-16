from fastapi import File, Form, Request, UploadFile
from fastapi.responses import HTMLResponse
from .config import router, templates
import os

@router.get("/")
async def hello(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "message" : "Olá, Ninja templates com FastAPI"}) 

@router.post("/home")
async def home(request: Request, email: str = Form(...)):
    pdf_directory = "static/pdf"
    pdf_files = os.listdir(pdf_directory)
    pdf_files = [f for f in pdf_files if f.endswith(".pdf")] #Filtra apenas arquivos pdf
    return templates.TemplateResponse("home.html", {"request" : request, "pdf_files" : pdf_files, "email" : email})

@router.post("/upload")
async def upload_file(request: Request, email: str = Form(...), file: UploadFile = File(...)):
    pdf_directory = "static/pdf"
    
    # Certifica-se de que a pasta existe
    os.makedirs(pdf_directory, exist_ok=True)
    
    # Salvar o arquivo
    file_path = os.path.join(pdf_directory, file.filename)  # Use file.filename em vez de file.file
    with open(file_path, "wb") as f:
        f.write(await file.read())
        
    # Redirecionar de volta para a página inicial
    return await home(request, email)
