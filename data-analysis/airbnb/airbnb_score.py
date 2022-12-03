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

def count_overlapping_features(in_gdf):
    # Get the name of the column containing the geometries
    geom_col = in_gdf.geometry.name
    
    # Setting up a single piece that will be split later
    input_parts = [in_gdf.unary_union.buffer(0)]
    
    # Finding all the "cutting" boundaries. Note: if the input GDF has 
    # MultiPolygons, it will treat each of the geometry's parts as individual
    # pieces.
    cutting_boundaries = []
    for i, row in in_gdf.iterrows():
        this_row_geom = row[geom_col]
        this_row_boundary = this_row_geom.boundary
        if this_row_boundary.type[:len('multi')].lower() == 'multi':
            cutting_boundaries = cutting_boundaries + list(this_row_boundary.geoms)
        else:
            cutting_boundaries.append(this_row_boundary)
    
    
    # Split the big input geometry using each and every cutting boundary
    for boundary in cutting_boundaries:
        splitting_results = []
        for j,part in enumerate(input_parts):
            new_parts = list(shapely.ops.split(part, boundary).geoms)
            splitting_results = splitting_results + new_parts
        input_parts = splitting_results
    
    # After generating all of the split pieces, create a new GeoDataFrame
    new_gdf = gpd.GeoDataFrame({'id':range(len(splitting_results)),
                                geom_col:splitting_results,
                                },
                               crs=in_gdf.crs,
                               geometry=geom_col)
    
    # Find the new centroids.
    new_gdf['geom_centroid'] = new_gdf.centroid
    
    # Starting the count at zero
    new_gdf['count_intersections'] = 0
    
    # For each of the `new_gdf`'s rows, find how many overlapping features 
    # there are from the input GDF.
    for i,row in new_gdf.iterrows():
        new_gdf.loc[i,'count_intersections'] = in_gdf.intersects(row['geom_centroid']).astype(int).sum()
        pass
    
    # Dropping the column containing the centroids
    new_gdf = new_gdf.drop(columns=['geom_centroid'])[['id','count_intersections',geom_col]]
    
    return new_gdf


# 1. filter with price range & room type
airbnb_filtered = filtering(up1.pr[0], up1.pr[1], up1.rt)
#filtered.to_csv("filtered_aribnb.csv" , index=False)

food = pd.read_csv('cleaned_food_amenities.csv')
gdfood = gpd.GeoDataFrame(food, geometry=gpd.points_from_xy(food.lon, food.lat))

local = gpd.read_file('local-area-boundary.geojson')
print(gdfood)
m=local.explore(style_kwds={'color':'black', 'opacity': 0})
#gdf.explore(m=m)

gdfood['geometry'] = gdfood.buffer(0.004)
gdfood.explore(m=m, style_kwds={'stroke':False, 'fillOpacity':0.5})

#Count the overlapping features of restaurant buffers
# food_intersections = count_overlapping_features(gdfood)
# food_intersections = food_intersections.sort_values('count_intersections', ascending=False)
# food_intersections.explore(m=m, style_kwds={'stroke':False, 'fillOpacity':0.5})
#food_intersections['geometry'] = food_intersections.centroid
#Plot results
#food_intersections[:10].explore(marker_type = 'circle', marker_kwds = {'radius':20, 'fill':True})

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
