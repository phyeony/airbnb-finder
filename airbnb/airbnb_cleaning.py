import pandas as pd

airbnb = pd.read_csv('airbnb_listings.csv.gz')

# Data cleaning - only using the data we need
airbnb = airbnb[['name', 'listing_url','neighbourhood', 'latitude', 'longitude', 'room_type', 'review_scores_rating']] 

# Export to a cleaned csv file
airbnb.to_csv("filtered_airbnb_listings.csv", index=False)

