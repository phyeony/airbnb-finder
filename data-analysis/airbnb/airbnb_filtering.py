import pandas as pd
import sys
import geopandas as gpd
from shapely.geometry import Point, Polygon
import shapely

def filtering(min_price, max_price, room_type):
    airbnb = pd.read_csv('cleaned_airbnb_data.csv')

    # "Entire home/apt"
    # "Hotel room"
    # "Private room"
    # "Shared room"
    
    # filter price range
    price_filtered = airbnb[(airbnb['price'] >= float(min_price)) & (airbnb['price'] <= float(max_price))]
    # filter room type
    filtered = price_filtered.loc[price_filtered['room_type'].isin(room_type)]
    return filtered

def count_overlapping_features(gdf: gpd.GeoDataFrame):
    #generating all of the split pieces
    import shapely
    bounds = gdf.geometry.exterior.unary_union
    new_polys = list(shapely.ops.polygonize(bounds))
    new_gdf = gpd.GeoDataFrame(geometry=new_polys, crs='epsg:32634')
    new_gdf['id'] = range(len(new_gdf))

    #count overlapping by sjoin between pieces centroid and the input gdf 
    new_gdf_centroid = new_gdf.copy()
    new_gdf_centroid['geometry'] = new_gdf.centroid
    overlapcount = gpd.sjoin(new_gdf_centroid,gdf)
    overlapcount = overlapcount.groupby(['id'])['index_right'].count().rename('count').reset_index()
    out_gdf = pd.merge(new_gdf,overlapcount)
    return out_gdf

class user_preference:
    def __init__(self, price_range, room_type, amenity):
        self.pr = price_range
        self.rt= room_type
        self.at = amenity

# pr = [0, 200]
# rt1 = ["Entire home/apt", "Hotel room"]
# rt2 = ["Private room"]
# rt3 = ["Entire home/apt", "Private room", "Shared room"]

# at1 = ["food"]
# at2 = ["transportation", "attraction"]

# # background map
# local = gpd.read_file('local-area-boundary.geojson')
# m=local.explore(style_kwds={'color':'black', 'opacity': 0})