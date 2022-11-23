import pandas as pd
import sys

airbnb = pd.read_csv('filtered_airbnb_listings.csv')

def main(min_price, max_price, room_type):
    # filter price range
    print("min price: ", min_price)
    print("max price: ", max_price)
    print("room type: ", room_type)
    print(airbnb)
    # filter room type

if __name__ == '__main__':
    min_price = sys.argv[1]
    max_price = sys.argv[2]
    room_type = sys.argv[3]
    main(min_price, max_price, room_type)