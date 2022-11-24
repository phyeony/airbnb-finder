import pandas as pd
import os

def compute_airbnb(user_preference):    
    ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))
    CLEANED_DATA_DIR = os.path.join(ROOT_DIR, 'cleaned_data')
    
    df = pd.read_csv(os.path.join(CLEANED_DATA_DIR, 'cleaned_airbnb_data.csv'))
    print(df)
    
    # Add logic to compute airbnb here base on user's preference
    return