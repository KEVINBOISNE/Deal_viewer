from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pathlib import Path

from deal_viewer1.database.db import database
from deal_viewer1.routes.health_check_router import router as health_check_router
from deal_viewer1.routes.get_deal import router as get_deal

from fastapi.middleware.cors import CORSMiddleware




from deal_viewer1.routes.template_router import router as template_router

app = FastAPI()

# Connect database
app.database = database

# chemin vers /front
BASE_DIR = Path(__file__).resolve().parents[2]
FRONT_DIR = BASE_DIR / "front"

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:8000"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

# servir les fichiers front
app.mount("/front", StaticFiles(directory=FRONT_DIR), name="front")

# page principale
@app.get("/")
def frontend():
    return FileResponse(FRONT_DIR / "index.html")

# routers API
app.include_router(health_check_router, prefix="/health-check", tags=["Health-check"])

app.include_router(get_deal, prefix="/get-deal", tags=["Get-deal"])

app.include_router(get_deal, prefix="/get-deal", tags=["Get-deal"])

app.include_router(template_router)
