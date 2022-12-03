#%%
import pandas as pd

df = pd.read_json(
    "output/sport/sport.json.gz", lines=True, compression="gzip"
)
#%%
df['type'].unique()
# array(['multi', 'yoga', 'skateboard', 'swimming', 'gymnastics', 'fitness',
#        'spinning', 'Lawn_bowling', 'pilates', 'curling', 'bowls',
#        'cycling', 'golf', 'rock_climbing', 'martial_arts', 'pool;fitness',
#        'billiards;darts', 'cycling;fitness', 'rowing', '10pin', 'boxing',
#        'ski', 'billiards', 'roller_hockey', 'hockey;ice_skating',
#        'running', 'soccer', 'climbing', 'swimming;fitness', 'disc_golf',
#        'dance', 'kickboxing;boxing', 'ice_climbing', 'basketball',
#        'crossfit',
#        'swimming;kickboxing;pilates;yoga;weightlifting;exercise',
#        'yoga;pilates', 'gymnastics;parkour', 'ice_hockey'], dtype=object)

# TODO: Keep

#%%
# https://towardsdatascience.com/all-pandas-json-normalize-you-should-know-for-flattening-json-13eae1dfb7dd
# print(amenities)
# print(amenities['amenity'].unique())
tags = pd.json_normalize(df["tags"])
unnested_df= pd.concat([df, tags], axis=1)

count = unnested_df.groupby(['type'])['type'].count()

# type
# 10pin                                                       1
# Lawn_bowling                                                1
# basketball                                                  1
# billiards                                                   1
# billiards;darts                                             2
# bowls                                                       1
# boxing                                                      1
# climbing                                                    3
# crossfit                                                    1
# curling                                                     2
# cycling                                                     3
# cycling;fitness                                             1
# dance                                                       1
# disc_golf                                                   1
# fitness                                                    16 # TODO: sport-fitness is only 16 but it was like 50 from leisure..
# golf                                                        1
# gymnastics                                                  6
# gymnastics;parkour                                          1
# hockey;ice_skating                                          1
# ice_climbing                                                3
# ice_hockey                                                  1
# kickboxing;boxing                                           1
# martial_arts                                                1
# multi                                                       1
# pilates                                                     1
# pool;fitness                                                1
# rock_climbing                                               1
# roller_hockey                                               1
# rowing                                                      1
# running                                                     2
# skateboard                                                  3
# ski                                                         1
# soccer                                                      2
# spinning                                                    1
# swimming                                                    2
# swimming;fitness                                            1
# swimming;kickboxing;pilates;yoga;weightlifting;exercise     1
# yoga                                                       19
# yoga;pilates                                                1
# Name: type, dtype: int64

#%%
# unnested_df.to_csv("cleaned_sport_amenities.csv", index=False)

## I think we can exclude sports.