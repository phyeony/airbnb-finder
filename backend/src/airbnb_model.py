from pydantic import BaseModel, root_validator, conlist
from typing import List, Literal

class Options(BaseModel):
    min_price: int = None
    max_price: int = None
    airbnb_room_type: conlist(Literal['Entire home/apt', 'Private room', 'Shared room', 'Hotel room'], min_items=1)
    activity_preference: List [Literal["entertainment", "food", "leisure", "transportation", "shop", "tourism"]]

    @root_validator
    def check_prices(cls, values):
        min_price, max_price = values.get('min_price'), values.get('max_price')
        if min_price > max_price:
            raise ValueError('max_price should be bigger than min_price.')
        if max_price > 20000:
            raise ValueError('Too expensive! No airbnbs above $20000 CAD. Lower max_price.')
        return values

# Doesn't seem to do validation. TODO: might wanna look into it more.
class AirbnbList(BaseModel):
    point: List[float]
    price: int
    address: str = None