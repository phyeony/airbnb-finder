#%%
import pandas as pd
import numpy as np

df = pd.read_json(
    "output/leisure/leisure.json.gz", lines=True, compression="gzip"
)
#%%

# df['type'].unique()

# array(['sports_centre', 'park', 'fitness_centre', 'dance', 'playground',
#        'swimming_pool', 'ice_rink', 'fitness_station', 'pitch', 'slipway',
#        'escape_game', 'marina', 'hackerspace', 'bowling_alley',
#        'Paintball', 'garden', 'golf_course', 'outdoor_seating', 'sauna',
#        'trampoline_park', 'disc_golf_course', 'amusement_arcade',
#        'indoor_play', 'sports_hall', 'dog_park', 'miniature_golf'],

# Remove 'prison', 'money_transfer', 'storage_rental', 'language_school', 

# osm_data = osm_data.replace(['bar', 'biergarten', 'cafe', 'fast_food', 'food_court', 'ice_cream', 'pub', 'restaurant'], 'sustenance')
# osm_data = osm_data.replace(['kick-scooter_rental', 'bicycle_rental', 'bus_station', 'car_rental', 'car_sharing', 'taxi'], 'transportation')
# osm_data = osm_data.replace(['bicycle_parking', 'motorcycle_parking', 'parking', 'parking_entrance', 'parking_space'], 'parking')

# Keep 
#  'cafe', 'fast_food', 'bbq', 'restaurant', 'pub', 'bar', 'ice_cream','food_court','bistro', 'biergarten'
#  'drinking_water' 'fountain'
#  'parking_space', 'parking', 'car_rental', 'car_sharing', 'motorcycle_parking', 'motorcycle_rental',
#  'cinema', 'theatre', 'nightclub', 'arts_centre', 'stripclub', 'boat_rental', 'gambling', 'marketplace', 'karaoke_box','spa', 'hookah_lounge','internet_cafe','casino','dance', 'toy_library',  'leisure'
#   
#  'bus_station', 'bicycle_parking', 'bicycle_rental', 'bicycle_repair_station', 'ferry_terminal',  'seaplane terminal'


# https://towardsdatascience.com/all-pandas-json-normalize-you-should-know-for-flattening-json-13eae1dfb7dd
# print(amenities)
# print(amenities['amenity'].unique())
tags = pd.json_normalize(amenities["tags"])
unnested_amenities = pd.concat([amenities, tags], axis=1)
print(unnested_amenities)
df = unnested_amenities[unnested_amenities['tourism'].notna()]
print(df)
# https://stackoverflow.com/questions/19913659/pandas-conditional-creation-of-a-series-dataframe-column
#  'cafe', 'fast_food', 'bbq', 'restaurant', 'pub', 'bar', 'ice_cream','food_court','bistro', 'biergarten'
# → Food

#  'parking_space', 'parking', 'car_rental', 'car_sharing', 'motorcycle_parking', 'motorcycle_rental',
# → Car

#  'cinema', 'theatre', 'nightclub', 'arts_centre', 'stripclub', 'boat_rental', 'gambling', 'marketplace', 'karaoke_box','spa', 'hookah_lounge','internet_cafe','casino','dance', 'toy_library',  'leisure' , … other tourist attraction
# -> Attraction

#  'bus_station', 'bicycle_parking', 'bicycle_rental', 'bicycle_repair_station', 'ferry_terminal',  'seaplane terminal'
# -> public transportatin

#%%

food_condition = (
    (amenities["amenity"] == "cafe")
    | (amenities["amenity"] == "fast_food")
    | (amenities["amenity"] == "bbq")
    | (amenities["amenity"] == "restaurant")
    | (amenities["amenity"] == "pub")
    | (amenities["amenity"] == "bar")
    | (amenities["amenity"] == "ice_cream")
    | (amenities["amenity"] == "food_court")
    | (amenities["amenity"] == "bistro")
    | (amenities["amenity"] == "biergarten")
)

attraction_condition = (
    (amenities["amenity"] == "cinema")
    | (amenities["amenity"] == "cinema")
    | (amenities["amenity"] == "theatre")
    | (amenities["amenity"] == "nightclub")
    | (amenities["amenity"] == "arts_centre")
    | (amenities["amenity"] == "stripclub")
    | (amenities["amenity"] == "boat_rental")
    | (amenities["amenity"] == "gambling")
    | (amenities["amenity"] == "marketplace")
    | (amenities["amenity"] == "spa")
    | (amenities["amenity"] == "hookah_lounge")
    | (amenities["amenity"] == "internet_cafe")
    | (amenities["amenity"] == "casino")
    | (amenities["amenity"] == "dance")
    | (amenities["amenity"] == "toy_library")
    | (amenities["amenity"] == "leisure")
)

# public_transportation_condition = (amenities['amenity'] == 'bus_station') \
#     or (amenities['amenity'] == 'bicycle_parking') \
#     or (amenities['amenity'] == 'bicycle_rental') \
#     or (amenities['amenity'] == 'bicycle_repair_station') \
#     or (amenities['amenity'] == 'ferry_terminal') \
#     or (amenities['amenity'] == ) \
#     or (amenities['amenity'] == ) \
#     or (amenities['amenity'] == ) \
#     or (amenities['amenity'] == ) \
#     or (amenities['amenity'] == ) \

# There's no train station. Maybe suse the stops.csv or station.csv

# For later use.
# attraction_condition =  (amenities['amenity'] == 'cinema') \
# or (amenities['amenity'] == ) \
# or (amenities['amenity'] == ) \
# or (amenities['amenity'] == ) \
# or (amenities['amenity'] == ) \
# or (amenities['amenity'] == ) \
# or (amenities['amenity'] == ) \
# or (amenities['amenity'] == ) \
# or (amenities['amenity'] == ) \
# or (amenities['amenity'] == ) \

conditions = [
    food_condition,
    attraction_condition,
]
choices = ["food", "attraction"]
amenities["category"] = np.select(conditions, choices, default=None)

#Keep amenities with category (food and attraction)
amenities = amenities[amenities['category'].notna()]
del amenities['timestamp']

food_amenities = amenities[amenities['category']=='food']
attraction_amenities = amenities[amenities['category']=='attraction']

food_amenities.to_csv("cleaned_food_amenities.csv", index=False)
attraction_amenities.to_csv("cleaned_attraction_amenities.csv", index=False)
# %%
