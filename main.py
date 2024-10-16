from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routes.web import router as web_router

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

#incluindo as rotas
app.include_router(web_router)