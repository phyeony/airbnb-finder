import sys
import pandas as pd
from ast import literal_eval
from shapely.geometry import Point, Polygon

# python points.py boundary.csv Stops.csv 
# python points.py boundary.csv Stations_Exchanges.csv

def main(bd, pt):
  boundary = pd.read_csv(bd)
  boundary['coordinates'] = boundary['coordinates'].apply(literal_eval)
  # lists to polygons
  def to_poly(x):
    x = x.apply(lambda x: Polygon(x))
    return x
  # clean the dataframe - only names and polygons
  boundary['poly'] = to_poly(boundary['coordinates'])
  del boundary['ID']
  del boundary['coordinates']
  
  # stops/stations&exchanges
  points = pd.read_csv(pt)
  
  # combine Longitudes and Latitudes together to a list
  points['Point'] = points['Longitude'].astype(str) + ", " +  points['Latitude'] .astype(str)
  points['Point'] = points['Point'].apply(lambda x: list(x.split(", ")))
  points['Point'] = points['Point'].apply(lambda x: list(map(float, x)))
  # clean the dataframe - remove x, y, lon, lat
  del points['x'], points['y'], points['Longitude'], points['Latitude']

  # Function that returns the boundary in which the point is included
  def which_boundary(p):
    stop = Point(p)
    boundary['contained'] = boundary['poly'].apply(lambda x: x.contains(stop))
    contained_boundary = (boundary.loc[boundary['contained'] == True])
    del boundary['contained']
    if len(contained_boundary.index) == 0:
      return "NB"
    boundary_name = contained_boundary['name'].iloc[0]
    return boundary_name

  # Apply the function
  points['boundary'] = points['Point'].apply(lambda x: which_boundary(x))
  
  # Exclude all the points that are not included in any boundary
  no_boundary = points[points['boundary'] == "NB"].index
  points = points.drop(no_boundary)

  if pt == 'Stops.csv':
    export_stop(points)
  if pt == 'Stations_Exchanges.csv':
    export_exchange(points)
    
# export
def export_stop(df):
  df.to_csv('Stops-with-boundary.csv', index=False)
def export_exchange(df):
  df.to_csv('Stations-with-boundary.csv', index=False)


if __name__ == '__main__':
    bd = sys.argv[1]
    pt = sys.argv[2]
    main(bd, pt)
