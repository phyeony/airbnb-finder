import pandas as pd
import sys

# python airbnb_filtering.py 100 200 private
def main(min_price, max_price, room_type):
    airbnb = pd.read_csv('filtered_airbnb_listings.csv')
    # Entire home/apt
    # Hotl room
    # Private room
    # Shared room
    # filter price range
    print(type(min_price))
    airbnb_priced = airbnb[(airbnb['price'] >= int(min_price)) & (airbnb['price'] <= int(max_price))]
    print(airbnb_priced[['name', 'price']])
    # filter room type

if __name__ == '__main__':
    min_price = sys.argv[1]
    max_price = sys.argv[2]
    room_type = sys.argv[3]
    main(min_price, max_price, room_type)