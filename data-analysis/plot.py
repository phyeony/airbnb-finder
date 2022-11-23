# pip install geopandas
# pip install folium matplotlib mapclassify
#%%
import sys
import pandas as pd
from ast import literal_eval
from shapely.geometry import Point, Polygon
import geopandas as gpd
#%%

gdf = gpd.read_file("local-area-boundary.geojson")
gdf.explore()
