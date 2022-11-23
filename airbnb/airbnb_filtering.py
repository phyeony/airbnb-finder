import pandas as pd
import sys

# python airbnb_filtering.py 100 200 private
def main(min_price, max_price, room_type):
    airbnb = pd.read_csv('cleaned_airbnb_listings.csv')

    if room_type == "entire":
        room_type = "Entire home/apt"
    elif room_type == "hotel":
        room_type = "Hotel room"
    elif room_type == "private":
        room_type = "Private room"
    elif room_type == "shared":
        room_type = "Shared room"
    # Entire home/apt
    # Hotel room
    # Private room
    # Shared room

    # filter price range
    price_filtered = airbnb[(airbnb['price'] >= float(min_price)) & (airbnb['price'] <= float(max_price))]
    # filter room type
    filtered = price_filtered[(price_filtered['room_type'] == room_type)]

    filtered.to_csv(min_price + '_to_' + max_price + '_' + room_type + "_filtered_aribnb.csv" , index=False)

if __name__ == '__main__':
    min_price = sys.argv[1]
    max_price = sys.argv[2]
    room_type = sys.argv[3]
    main(min_price, max_price, room_type)