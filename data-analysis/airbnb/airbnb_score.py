#%%
import pandas as pd
import sys
from airbnb_filtering import filtering, count_overlapping_features, user_preference
import matplotlib.pyplot as plt
import geopandas as gpd
from shapely.geometry import Point, Polygon
import shapely

# 1. filter with amenities - get intersection scores
# food
food = pd.read_csv('cleaned_food_amenities.csv')
gdfood = gpd.GeoDataFrame(food, geometry=gpd.points_from_xy(food.lon, food.lat), crs='epsg:4326')
gdfood = gdfood.to_crs("EPSG:32634")
gdfood['geometry'] = gdfood.buffer(300, 3)

# Count the overlapping features of restaurant buffers
food_intersections = count_overlapping_features(gdfood)
avg = food_intersections['count'].mean()
food_intersections = food_intersections.sort_values('count', ascending=False)
food_intersections['geometry'] = food_intersections.centroid
over_avg = food_intersections[food_intersections['count'] >= avg]

# - for each intersection,
    # (1) get amneity intersection points
    # (2) give a boundary for each intersection
    # (3) if an airbnb is in the intersection, give it a point
        # (3)-a adds another column to the airbnb_filtered list with each point

# 2. 

# %%
