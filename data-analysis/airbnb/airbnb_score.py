import pandas as pd
import sys
from airbnb_filtering import filtering

class user_preference:
    def __init__(self, price_range, room_type, amenity):
        self.pr = price_range
        self.rt= room_type
        self.at = amenity

def main(up1):
    filtered = filtering(up1.pr[0], up1.pr[1], up1.rt)
    filtered.to_csv("filtered_aribnb.csv" , index=False)
    print(filtered, up1.at)

if __name__ == '__main__':
    min_p = sys.argv[1]
    max_p = sys.argv[2]
    pr = [min_p, max_p]
    rt1 = ["Entire home/apt", "Hotel room"]
    rt2 = ["Private room"]
    rt3 = ["Entire home/apt", "Private room", "Shared room"]

    at1 = ["transportation"]
    at2 = ["food", "attraction"]
    up1 = user_preference(pr, rt1, at1)
    main(up1)

#python airbnb_score.py 100 200


