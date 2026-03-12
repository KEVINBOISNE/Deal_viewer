from fastapi import FastAPI
from deal_viewer1.database.db import database
from deal_viewer1.routes.health_check_router import router as health_check_router
from deal_viewer1.routes.insert_template import router as insert_template
from deal_viewer1.routes.update_template import router as update_template
from deal_viewer1.routes.delete_template import router as delete_template

app = FastAPI()

#Connect database
app.database = database

app.include_router(health_check_router, prefix="/health-check", tags=["Health-check"])
app.include_router(insert_template, prefix="/insert-template", tags=["Insert-template"])
app.include_router(update_template, prefix="/update-template", tags=["Update-Template"])
app.include_router(delete_template, prefix="/delete-template", tags=["Delete-Template"])


