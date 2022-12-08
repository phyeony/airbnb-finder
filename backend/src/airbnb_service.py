import pandas as pd
import os
from .airbnb_model import Options
from operator import itemgetter

def compute_airbnb(user_preference: Options) -> pd.DataFrame:    
    ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))
    CLEANED_DATA_DIR = os.path.join(ROOT_DIR, 'data')
    
    df = pd.read_csv(os.path.join(CLEANED_DATA_DIR, 'airbnb_score.csv'))
    
    min_price, max_price, airbnb_room_type, activity_preference = itemgetter('min_price','max_price', 'airbnb_room_type', 'activity_preference')(user_preference.dict())

    # Filter with room type
    # ['Entire home/apt', 'Private room', 'Shared room', 'Hotel room']
    df = df[df['room_type'].isin(airbnb_room_type)] 

    # Filter with price range
    if min_price is not None and max_price is not None:
        df = df[(df['price'] >= min_price) & (df['price'] <= max_price)]
    elif min_price is not None:
        df = df[df['price'] >= min_price]
    elif max_price is not None:
        df = df[df['price'] <= max_price]

    # Filter with acitivity preference 
    # TODO
    
    

    df = df.head(10)
    
    # Add logic to compute airbnb here base on user's preference
    return df