#%%
import pandas as pd
import sys
from airbnb_filtering import filtering, count_overlapping_features, user_preference
import matplotlib.pyplot as plt
import geopandas as gpd
from shapely.geometry import Point, Polygon
import shapely

airbnb = pd.read_csv('cleaned_airbnb_data.csv')

def intersection_score(airbnb, amenity):
    #  1) get all amenity intersection points(coordinates) -> return only with points with intersection counts bigger than average count
    amen = pd.read_csv(amenity)
    gdamen = gpd.GeoDataFrame(amen, geometry=gpd.points_from_xy(amen.lon, amen.lat), crs='epsg:4326')
    gdamen = gdamen.to_crs("EPSG:32634")
    gdamen['geometry'] = gdamen.buffer(300, 3)

    # Count the overlapping features of restaurant buffers
    amen_intersections = count_overlapping_features(gdamen)
    avg = amen_intersections['count'].mean()
    amen_intersections = amen_intersections.sort_values('count', ascending=False)
    amen_intersections['geometry'] = amen_intersections.centroid
    over_avg = amen_intersections[amen_intersections['count'] >= avg]
    #  2) give a boundary for each intersection
    over_avg['geometry'] = over_avg.buffer(300, 3)
    # 3) if an airbnb is in the intersection, give it a point
    return over_avg



airbnb = intersection_score(airbnb, 'cleaned_food_amenities.csv')
#  4) adds another column to the airbnb data with each intersection score


# - for each intersection,
    # (1) get amneity intersection points
    # (2) give a boundary for each intersection
    # (3) if an airbnb is in the intersection, give it a point
        # (3)-a adds another column to the airbnb_filtered list with each point

# 2. 

# %%
