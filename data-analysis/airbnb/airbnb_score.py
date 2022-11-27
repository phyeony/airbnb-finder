#%%
import pandas as pd
import sys
from airbnb_filtering import filtering
import geopandas as gpd
from shapely.geometry import Point, Polygon
import contextily as cx
import osmnx as ox
import shapely
import matplotlib.pyplot as plt

class user_preference:
    def __init__(self, price_range, room_type, amenity):
        self.pr = price_range
        self.rt= room_type
        self.at = amenity

pr = [0, 200]
rt1 = ["Entire home/apt", "Hotel room"]
rt2 = ["Private room"]
rt3 = ["Entire home/apt", "Private room", "Shared room"]

at1 = ["food"]
at2 = ["transportation", "attraction"]

up1 = user_preference(pr, rt2, at1)

# 1. filter with price range & room type
airbnb_filtered = filtering(up1.pr[0], up1.pr[1], up1.rt)
#filtered.to_csv("filtered_aribnb.csv" , index=False)

food = pd.read_csv('cleaned_food_amenities.csv')
gdf = gpd.GeoDataFrame(food, geometry=gpd.points_from_xy(food.lon, food.lat))

local = gpd.read_file('local-area-boundary.geojson')
m=local.explore()
gdf.explore(m=m)

#gdf.explore(m=m)
# 2. filter with amenities
# 1) for each intersection,
    # (1) get amneity intersection points
    # (2) give a boundary for each intersection
    # (3) if an airbnb is in the intersection, give it a point
        # (3)-a adds another column to the airbnb_filtered list with each point
# 2) 
#print(airbnb_filtered, up1.at)


# %%
