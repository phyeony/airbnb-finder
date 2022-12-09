import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import shapely

def count_overlapping_features(gdf: gpd.GeoDataFrame):
    #generating all of the split pieces
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

def amentiy_intersections(amenity: str):
    #  1) get all amenity intersection points(coordinates) -> return only with points with intersection counts bigger than average count
    amen = pd.read_csv(f'cleaned_data/{amenity}')
    gdamen = gpd.GeoDataFrame(amen, geometry=gpd.points_from_xy(amen.lon, amen.lat), crs='epsg:4326')
    gdamen = gdamen.to_crs("EPSG:32634")
    gdamen['geometry'] = gdamen.buffer(300, 3)

    # Count the overlapping features of restaurant buffers
    amen_intersections = count_overlapping_features(gdamen)
    avg = amen_intersections['count'].mean()
    amen_intersections = amen_intersections.sort_values('count', ascending=False)
    amen_intersections['geometry'] = amen_intersections.centroid
    over_avg = amen_intersections[amen_intersections['count'] >= avg]
    #  2) give a boundary for each intersection point
    over_avg['geometry'] = over_avg.buffer(300, 3)

    split = list(amenity.split("_"))
    name = list(split[1].split("."))
    name = name[0]
    over_avg.to_csv(name + '_intersection.csv', index=False)
    return over_avg, name

def intersection_score(airbnb: pd.DataFrame, amen_intersections: gpd.GeoDataFrame, name: str):
    # 3) if an airbnb is in the intersection, give it a point
    gd_airbnb = gpd.GeoDataFrame(airbnb, geometry=gpd.points_from_xy(airbnb.longitude, airbnb.latitude), crs='epsg:4326')
    gd_airbnb = gd_airbnb.to_crs("EPSG:32634")
    #  4) adds another column to the airbnb data with each intersection score
    gd_airbnb[name] = gd_airbnb['geometry'].apply(lambda x:score(x, amen_intersections))
    gd_airbnb = gd_airbnb.to_crs('epsg:4326')
    gd_airbnb = gd_airbnb.drop(columns=['geometry'])
    return gd_airbnb

def score(point: Point, intersections: gpd.GeoDataFrame):
    contain = intersections['geometry'].contains(point)
    intersections['contain'] = contain
    intersections = intersections[intersections['contain'] == True]
    if len(intersections) != 0:
        tf = intersections.groupby('contain').agg(count_sum=pd.NamedAgg(column='count', aggfunc='sum'))
        return tf['count_sum'][0]
    else:
        return 0

# background map
# local = gpd.read_file('local-area-boundary.geojson')
# m=local.explore(style_kwds={'color':'black', 'opacity': 0})
