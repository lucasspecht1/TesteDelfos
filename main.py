import uvicorn
from src.server import router
from fastapi import FastAPI

app = FastAPI()
app.include_router(router, prefix='/database')