#%%
import pandas as pd

df = pd.read_json(
    "output/tourism/tourism.json.gz", lines=True, compression="gzip"
)
#%%
df['type'].unique()

# array(['artwork', 'museum', 'attraction', 'viewpoint', 'gallery',
#        'guest_house', 'house', 'camp_site', 'Plane_Spotting_Platform',
#        'wilderness_hut'], dtype=object)

# TODO: delete
# Delete 'guest_house'

#%%
# https://towardsdatascience.com/all-pandas-json-normalize-you-should-know-for-flattening-json-13eae1dfb7dd
# print(amenities)
# print(amenities['amenity'].unique())
tags = pd.json_normalize(df["tags"])
unnested_df= pd.concat([df, tags], axis=1)

count = unnested_df.groupby(['type'])['type'].count()

# type
# Plane_Spotting_Platform      1
# artwork                    200
# attraction                  26
# camp_site                    1
# gallery                     20
# guest_house                 18
# house                        1
# museum                      16
# viewpoint                   40
# wilderness_hut               1
# Name: type, dtype: int64


#%%
unnested_df.to_csv("cleaned_tourism_amenities.csv", index=False)
# %%
