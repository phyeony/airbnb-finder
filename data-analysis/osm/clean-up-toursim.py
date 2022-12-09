#%%
import pandas as pd

df = pd.read_json(
    "output/tourism/tourism.json.gz", lines=True, compression="gzip"
)
#%%
df['type'].unique()

# array(['artwork', 'attraction', 'museum', 'guest_house', 'viewpoint', 
# 'gallery', 'Plane_Spotting_Platform'], dtype=object)

#%%
# https://towardsdatascience.com/all-pandas-json-normalize-you-should-know-for-flattening-json-13eae1dfb7dd
# print(amenities)
# print(amenities['amenity'].unique())
tags = pd.json_normalize(df["tags"])
unnested_df= pd.concat([df, tags], axis=1)

count = unnested_df.groupby(['type'])['type'].count()

# type
# Plane_Spotting_Platform      1
# artwork                    183
# attraction                  19
# gallery                     12
# guest_house                 16
# museum                       9
# viewpoint                   15
# Name: type, dtype: int64

tourism_condition = (
    (df["type"] == "artwork")
    | (df["type"] == "attraction")
    | (df["type"] == "museum")
    | (df["type"] == "viewpoint")
    | (df["type"] == "gallery")
    | (df["type"] == "Plane_Spotting_Platform")
)

tourism_df = df[tourism_condition]

#%%
tourism_df.to_csv("cleaned_tourism.csv", index=False)
# %%
