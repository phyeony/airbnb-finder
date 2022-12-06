#%%
import pandas as pd

df = pd.read_json(
    "output/leisure/leisure.json.gz", lines=True, compression="gzip"
)
#%%
df['type'].unique()

# # array(['sports_centre', 'swimming_pool', 'dance', 'fitness_centre',
#        'music_venue', 'ice_rink', 'fitness_station', 'pitch',
#        'playground', 'escape_game', 'marina', 'park', 'hackerspace',
#        'bowling_alley', 'garden', 'golf_course', 'outdoor_seating',
#        'sauna', 'amusement_arcade', 'indoor_play', 'sports_hall',
#        'dog_park', 'miniature_golf'], dtype=object)

# Keep 

#%%
# https://towardsdatascience.com/all-pandas-json-normalize-you-should-know-for-flattening-json-13eae1dfb7dd
# print(amenities)
# print(amenities['amenity'].unique())
tags = pd.json_normalize(df["tags"])
unnested_df= pd.concat([df, tags], axis=1)

count = unnested_df.groupby(['type'])['type'].count()
count
# type
# amusement_arcade     3
# bowling_alley        3
# dance                8
# dog_park             1
# escape_game          7
# fitness_centre      86
# fitness_station     11
# garden              13
# golf_course          1
# hackerspace          2
# ice_rink             2
# indoor_play          1
# marina               3
# miniature_golf       1
# music_venue          1
# outdoor_seating      1
# park                 3
# pitch                4
# playground           1
# sauna                1
# sports_centre       10
# sports_hall          1
# swimming_pool        2
# Name: type, dtype: int64

leisure_condition = (
    (df["type"] == "sports_centre")
    | (df["type"] == "swimming_pool")
    | (df["type"] == "dance")
    | (df["type"] == "fitness_centre")
    | (df["type"] == "music_venue")
    | (df["type"] == "ice_rink")
    | (df["type"] == "fitness_station")
    | (df["type"] == "pitch")
    | (df["type"] == "playground")
    | (df["type"] == "escape_game")
    | (df["type"] == "marina")
    | (df["type"] == "park")
    | (df["type"] == "hackerspace")
    | (df["type"] == "bowling_alley")
    | (df["type"] == "garden")
    | (df["type"] == "golf_course")
    | (df["type"] == "outdoor_seating")
    | (df["type"] == "sauna")
    | (df["type"] == "amusement_arcade")
    | (df["type"] == "indoor_play")
    | (df["type"] == "sports_hall")
    | (df["type"] == "dog_park")
    | (df["type"] == "miniature_golf")
)

leisure_df = df[leisure_condition]

#%%
leisure_df.to_csv("cleaned_leisure_amenities.csv", index=False)
# %%
