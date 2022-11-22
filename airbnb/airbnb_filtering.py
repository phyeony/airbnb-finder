import pandas as pd

airbnb = pd.read_csv('airbnb/filtered_airbnb_listings.csv')

def main(min_price, max_price):
    # filter price range
    
    # filter room type

if __name__ == '__main__':
    min_price = sys.argv[1]
    max_price = sys.argv[2]
    room_type = sys.argv[3]
    main(min_price, max_price)