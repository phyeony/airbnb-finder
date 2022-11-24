# from backend.src.service.aribnb_service import hi
from fastapi import APIRouter
from pydantic import BaseModel
from typing import (
    Deque, Dict, FrozenSet, List, Optional, Sequence, Set, Tuple, Union
)

from .airbnb_service import compute_airbnb


router = APIRouter()

class Options(BaseModel):
    airbnb_price_range: List[int] = None    # [100, 300]
    airbnb_room_type: List[str]  # ["Room A", "Room B"]
    amenity_preference: List [str]    # ["Food", "Attraction"]

# Doesn't seem to do validation. TODO: might wanna look into it more.
class AirbnbList(BaseModel):
    point: List[float]
    price: int
    address: str = None


@router.post("/airbnb_list", tags=["airbnb"])
async def get_airbnb_list(user_preference: Options) -> AirbnbList:
    print(compute_airbnb(user_preference))
    return {"point": ["123.343","-23.342"], "price": 432, "address":"this street, bc,canada"}