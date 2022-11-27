import pandas as pd
import sys

def filtering(min_price, max_price, room_type):
    airbnb = pd.read_csv('cleaned_airbnb_data.csv')

    # "Entire home/apt"
    # "Hotel room"
    # "Private room"
    # "Shared room"
    
    # filter price range
    price_filtered = airbnb[(airbnb['price'] >= float(min_price)) & (airbnb['price'] <= float(max_price))]
    # filter room type
    filtered = price_filtered.loc[price_filtered['room_type'].isin(room_type)]
    return filtered