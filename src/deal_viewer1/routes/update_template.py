from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List
from bson import ObjectId

router = APIRouter()

@router.put("/{id}", response_description="Update template")
def update_student(id: str, request: Request, template: dict = Body(...)):
    template = {k: v for k, v in template.items() if v is not None}
    if len(template) >= 1:
        update_result = request.app.database["template"].update_one(
        {"_id": ObjectId(id)}, {"$set": template}
    )
    
    if update_result.modified_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"template with ID {id} not found")

    
    existing_template = request.app.database["template"].find_one({"_id": ObjectId(id)})
    if existing_template:
       
        existing_template["_id"] = str(existing_template["_id"])
        return existing_template
        

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"template with ID {id} not found")