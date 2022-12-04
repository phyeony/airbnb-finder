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
    column_name = list(amenity.split("_"))
    column_name = column_name[1] + "_intersection_score"

    airbnb['point'] = airbnb['longitude'].astype(str) + ", " +  airbnb['latitude'] .astype(str)
    airbnb['point'] = airbnb['point'].apply(lambda x: list(x.split(", ")))
    airbnb['point'] = airbnb['point'].apply(lambda x: list(map(float, x)))
    airbnb['point'] = airbnb['point'].apply(lambda x: Point(x))

    print(over_avg)
    airbnb[column_name] = airbnb['point'].apply(lambda x:score(x, over_avg))
    del airbnb['point']
    return airbnb

def score(point: Point, intersections: gpd.GeoDataFrame):
    intersections['included'] = intersections['geometry'].apply(lambda x:x.contains(point))
    intersections = intersections[intersections['included'] == True]
    
    return score

airbnb_int = intersection_score(airbnb, 'cleaned_food_amenities.csv')
print(airbnb_int)
#  4) adds another column to the airbnb data with each intersection score


# - for each intersection,
    # (1) get amneity intersection points
    # (2) give a boundary for each intersection
    # (3) if an airbnb is in the intersection, give it a point
        # (3)-a adds another column to the airbnb_filtered list with each point

# 2. 

# %%
