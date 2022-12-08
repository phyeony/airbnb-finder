from fastapi import APIRouter
from fastapi import Response

from .airbnb_service import compute_airbnb
from .airbnb_model import Options, AirbnbList

router = APIRouter()

@router.post("/airbnb_list", tags=["airbnb"])
async def get_airbnb_list(user_preference: Options) -> AirbnbList:
    return Response(compute_airbnb(user_preference).to_json(orient="records"), media_type="application/json")