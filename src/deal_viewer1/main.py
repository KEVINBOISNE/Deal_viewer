from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pathlib import Path

from deal_viewer1.database.db import database
from deal_viewer1.routes.health_check_router import router as health_check_router
from deal_viewer1.routes.insert_template import router as insert_template
from deal_viewer1.routes.update_template import router as update_template
from deal_viewer1.routes.delete_template import router as delete_template
from deal_viewer1.routes.get_deal import router as get_deal

from fastapi.middleware.cors import CORSMiddleware


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
app.include_router(insert_template, prefix="/insert-template", tags=["Insert-template"])
app.include_router(update_template, prefix="/update-template", tags=["Update-Template"])
app.include_router(delete_template, prefix="/delete-template", tags=["Delete-Template"])
app.include_router(get_deal, prefix="/get-deal", tags=["Get-deal"])