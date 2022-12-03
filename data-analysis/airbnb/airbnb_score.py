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

def count_overlapping_features(gdf):
    #generating all of the split pieces
    import shapely
    bounds = gdf.geometry.exterior.unary_union
    new_polys = list(shapely.ops.polygonize(bounds))
    new_gdf = gpd.GeoDataFrame(geometry=new_polys)
    new_gdf['id'] = range(len(new_gdf))

    #count overlapping by sjoin between pieces centroid and the input gdf 
    new_gdf_centroid = new_gdf.copy()
    new_gdf_centroid['geometry'] = new_gdf.centroid
    overlapcount = gpd.sjoin(new_gdf_centroid,gdf)
    overlapcount = overlapcount.groupby(['id'])['index_right'].count().rename('count').reset_index()
    out_gdf = pd.merge(new_gdf,overlapcount)
    return out_gdf


# 1. filter with price range & room type
airbnb_filtered = filtering(up1.pr[0], up1.pr[1], up1.rt)
#filtered.to_csv("filtered_aribnb.csv" , index=False)

local = gpd.read_file('local-area-boundary.geojson')
m=local.explore(style_kwds={'color':'black', 'opacity': 0})

#food = pd.read_csv('cleaned_food_amenities copy.csv')
food = pd.read_csv('foods_.csv')
gdfood = gpd.GeoDataFrame(food, geometry=gpd.points_from_xy(food.lon, food.lat), crs='epsg:4326')
gdfood = gdfood.to_crs("EPSG:32634")


#gdf.explore(m=m)
gdfood['geometry'] = gdfood.buffer(300, 3)
#gdfood.explore(m=m, style_kwds={'stroke':False, 'fillOpacity':0.5})

# Count the overlapping features of restaurant buffers
food_intersections = count_overlapping_features(gdfood)
food_intersections = food_intersections.sort_values('count', ascending=False)
food_intersections['geometry'] = food_intersections.centroid
food_intersections = food_intersections[food_intersections['count'] >= 50]

# Plot results
food_intersections.explore(m=m, marker_type = 'circle', marker_kwds = {'radius':30, 'fill':True})
#gdfood.explore(m=m, style_kwds={'stroke':False, 'fillOpacity':0.5})
# 2. filter with amenities
# 1) for each intersection,
    # (1) get amneity intersection points
    # (2) give a boundary for each intersection
    # (3) if an airbnb is in the intersection, give it a point
        # (3)-a adds another column to the airbnb_filtered list with each point
# 2) 
#print(airbnb_filtered, up1.at)


# %%
