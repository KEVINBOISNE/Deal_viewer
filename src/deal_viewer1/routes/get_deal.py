from fastapi import APIRouter, Request, HTTPException, status
from fastapi.encoders import jsonable_encoder

router = APIRouter()

@router.get("/", response_description="Get all deals")
async def get_deals(request: Request):
    try:
        # Récupérer tous les deals de la DB
        deals_cursor = request.app.database["deal"].find()
        deals = []
        async for deal in deals_cursor:
            # Convertir ObjectId en str pour JSON
            deal["_id"] = str(deal["_id"])
            deals.append(deal)
        
        return deals

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))