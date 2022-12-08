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
    # ["entertainment", "food", "leisure", "transportation", "shop", "tourism"]
    # TODO FINISH Weight 
    # weight_1 = [1]
    # weight_2 = [1.25, 1]
    # weight_3 = [1.5, 1.25, 1]
    # weight_4 = [1.75, 1.5, 1.25, 1]
    # weight_5 = [2, 1.75, 1.5, 1.25, 1]
    # weight_6 = [2.25, 2, 1.75, 1.5, 1.25, 1]
    if len(activity_preference) > 0:
        weight = []
        for i in range(len(activity_preference)):
            # insert the value at index 0
            weight.insert(0, i * 0.25 + 1) 
        print("WEIGHT: ", weight)
        # https://stackoverflow.com/questions/18419962/how-to-compute-weighted-sum-of-all-elements-in-a-row-in-pandas
        df['weighted_sum'] = df[activity_preference].dot(weight)
        # Give weight of 1 to the airbnb review ratings
        df['weighted_sum'] = df[['weighted_sum', 'review_scores_rating']].sum(axis=1)
        # sort value with points
        df = df.sort_values('weighted_sum', ascending=False)
    else:
        df = df.sort_values('review_scores_rating', ascending=False)

    df = df.head(20)
    
    # Add logic to compute airbnb here base on user's preference
    return df