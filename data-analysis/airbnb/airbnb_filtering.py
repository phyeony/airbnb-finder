#%%
import pandas as pd
import sys
import geopandas as gpd
from shapely.geometry import Point, Polygon
import shapely
import airbnb_intersection as inters

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


# # cleaned_entertainment.csv
# airbnb = pd.read_csv('cleaned_airbnb_data.csv')
# amen_intersection, name = inters.amentiy_intersections('cleaned_entertainment.csv')
# intersection_airbnb = inters.intersection_score(airbnb, amen_intersection, name)
# intersection_airbnb.to_csv('airbnb_' + name[0] +'.csv', index=False) # -> airbnb_e.csv with entertainment

# # cleaned_food.csv
# # airbnb = intersection_airbnb
# airbnb = pd.read_csv('airbnb_e.csv')
# amen_intersection, name = inters.amentiy_intersections('cleaned_food.csv')
# intersection_airbnb = inters.intersection_score(airbnb, amen_intersection, name)
# intersection_airbnb.to_csv('airbnb_e' + name[0] +'.csv', index=False) # -> airbnb_ef.csv with entertainment,food

# # cleaned_leisure.csv
# # airbnb = intersection_airbnb
# airbnb = pd.read_csv('airbnb_ef.csv')
# amen_intersection, name = inters.amentiy_intersections('cleaned_leisure.csv')
# intersection_airbnb = inters.intersection_score(airbnb, amen_intersection, name)
# intersection_airbnb.to_csv('airbnb_ef' + name[0] +'.csv', index=False) # -> airbnb_food.csv with entertainment,food,leisure

# # cleaned_transportation.csv
# # airbnb = intersection_airbnb
# airbnb = pd.read_csv('airbnb_efl.csv')
# amen_intersection, name = inters.amentiy_intersections('cleaned_transportation.csv')
# intersection_airbnb = inters.intersection_score(airbnb, amen_intersection, name)
# intersection_airbnb.to_csv('airbnb_efl' + name[0] +'.csv', index=False) # -> airbnb_food.csv with entertainment,food,leisure,transportation

# # cleaned_shop.csv
# # airbnb = intersection_airbnb
# airbnb = pd.read_csv('airbnb_eflt.csv')
# amen_intersection, name = inters.amentiy_intersections('cleaned_shop.csv')
# intersection_airbnb = inters.intersection_score(airbnb, amen_intersection, name)
# intersection_airbnb.to_csv('airbnb_eflt' + name[0] +'.csv', index=False) # -> airbnb_food.csv with entertainment,food,leisure,transportation,shop

# cleaned_tourism.csv
# airbnb = intersection_airbnb
# airbnb = pd.read_csv('airbnb_eflts.csv')
# amen_intersection, name = inters.amentiy_intersections('cleaned_tourism.csv')
# intersection_airbnb = inters.intersection_score(airbnb, amen_intersection, name)
# intersection_airbnb.to_csv('airbnb_score.csv', index=False) # -> airbnb_food.csv with entertainment,food,leisure,transportation,shop,tourism

# pr = [0, 200]
# rt1 = ["Entire home/apt", "Hotel room"]
# rt2 = ["Private room"]
# rt3 = ["Entire home/apt", "Private room", "Shared room"]

# at1 = ["food"]
# at2 = ["transportation", "attraction"]

# background map
# local = gpd.read_file('local-area-boundary.geojson')
# m=local.explore(style_kwds={'color':'black', 'opacity': 0})
# %%
