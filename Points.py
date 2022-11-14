import pandas as pd
import numpy as numpy
from shapely.geometry import Point, Polygon

df = pd.read_json('local-area-boundary.json')
# boundary = df.loc[0,'fields']['geom']['coordinates']
# print(boundary)
# p1 = Point(-122.948947, 49.200056)
# coords = boundary[0]
# poly = Polygon(coords)

# print(p1.within(poly))


#     name        mapid coordinates
# 0 Arubutus-ridge AR     {[x,y], [x,y],....}
# 1 Downton       DT  {[x,y], [x,y],....}
# 2 Fairtown      SDS {[x,y], [x,y],....}