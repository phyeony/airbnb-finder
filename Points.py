import pandas as pd
import numpy as numpy
from shapely.geometry import Point, Polygon

df = pd.read_csv('boundary.csv')
coords = df['coordinates']

print(type(coords[0]))
poly = Polygon(coords[0])
print(poly)

# boundary = df.loc[0,'fields']['geom']['coordinates']
# print(boundary)
# p1 = Point(-122.948947, 49.200056)

# poly = Polygon(coords)
# print(poly)

# print(p1.within(poly))


#     name        mapid coordinates
# 0 Arubutus-ridge AR     {[x,y], [x,y],....}
# 1 Downton       DT  {[x,y], [x,y],....}
# 2 Fairtown      SDS {[x,y], [x,y],....}