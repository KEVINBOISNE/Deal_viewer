from fastapi import APIRouter, Request, Response, HTTPException, status
from bson import ObjectId

router = APIRouter()


@router.delete("/{id}", response_description="Delete a template")
def delete_book(id: str, request: Request, response: Response):
    delete_result = request.app.database["template"].delete_one({"_id": ObjectId(id)})

    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with ID {id} not found")
