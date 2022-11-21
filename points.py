import sys
import pandas as pd
from ast import literal_eval
from shapely.geometry import Point, Polygon
import os

# python points.py boundary.csv Stops.csv 
# python points.py boundary.csv Stations.csv

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
  # https://stackoverflow.com/questions/43898035/pandas-combine-column-values-into-a-list-in-a-new-column
  points['Point'] = points[['Longitude','Latitude']].values.tolist()

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

  points.to_csv(f"{os.path.splitext(pt)[0]}-with-boundary.csv", index=False)
  
if __name__ == '__main__':
    bd = sys.argv[1]
    pt = sys.argv[2]
    main(bd, pt)
