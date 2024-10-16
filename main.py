from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routes.web import router as web_router
from routes.auth import router as auth_router

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

#incluindo as rotas
app.include_router(web_router)
app.include_router(auth_router)