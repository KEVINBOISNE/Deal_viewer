from fastapi import APIRouter, Body, Request, status
from fastapi.encoders import jsonable_encoder
router = APIRouter()

@router.post("/", response_description="Create template", status_code=status.HTTP_201_CREATED)
def create_template(request: Request, template = Body(...)):
    template = jsonable_encoder(template)
    new_template = request.app.database["template"].insert_one(template)
    insert_template = request.app.database["template"].find_one(
        {"_id": new_template.inserted_id}
    )

    return insert_template
