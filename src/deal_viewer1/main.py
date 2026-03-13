from fastapi import FastAPI
from deal_viewer1.database.db import database
from deal_viewer1.routes.health_check_router import router as health_check_router
from deal_viewer1.routes.get_deal import router as get_deal



from deal_viewer1.routes.template_router import router as template_router

app = FastAPI()

#Connect database
app.database = database

app.include_router(health_check_router, prefix="/health-check", tags=["Health-check"])

app.include_router(get_deal, prefix="/get-deal", tags=["Get-deal"])

app.include_router(template_router)
