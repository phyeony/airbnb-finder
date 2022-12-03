#%%
import pandas as pd

df = pd.read_json(
    "output/leisure/leisure.json.gz", lines=True, compression="gzip"
)
#%%
df['type'].unique()

# array(['sports_centre', 'park', 'fitness_centre', 'dance', 'playground',
#        'swimming_pool', 'ice_rink', 'fitness_station', 'pitch', 'slipway',
#        'escape_game', 'marina', 'hackerspace', 'bowling_alley',
#        'Paintball', 'garden', 'golf_course', 'outdoor_seating', 'sauna',
#        'trampoline_park', 'disc_golf_course', 'amusement_arcade',
#        'indoor_play', 'sports_hall', 'dog_park', 'miniature_golf'],

# Keep 

#%%
# https://towardsdatascience.com/all-pandas-json-normalize-you-should-know-for-flattening-json-13eae1dfb7dd
# print(amenities)
# print(amenities['amenity'].unique())
tags = pd.json_normalize(df["tags"])
unnested_df= pd.concat([df, tags], axis=1)

count = unnested_df.groupby(['type'])['type'].count()

# type
# Paintball             1
# amusement_arcade      3
# bowling_alley         4
# dance                16
# disc_golf_course      1
# dog_park              1
# escape_game           8
# fitness_centre      126
# fitness_station      11
# garden               13
# golf_course           3
# hackerspace           1
# ice_rink              3
# indoor_play           2
# marina                3
# miniature_golf        1
# outdoor_seating       1
# park                  7
# pitch                 5
# playground            3
# sauna                 1
# slipway               1
# sports_centre        16
# sports_hall           3
# swimming_pool         3
# trampoline_park       1
# Name: type, dtype: int64


#%%
unnested_df.to_csv("cleaned_leisure_amenities.csv", index=False)