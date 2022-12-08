#%%
import pandas as pd
import airbnb_intersection as inters
    
# # cleaned_entertainment.csv
# airbnb = pd.read_csv('cleaned_data/cleaned_airbnb_data.csv')
# amen_intersection, name = inters.amentiy_intersections('cleaned_entertainment.csv')
# intersection_airbnb = inters.intersection_score(airbnb, amen_intersection, name)
# intersection_airbnb.to_csv('airbnb_' + name[0] +'.csv', index=False) # -> airbnb_e.csv with entertainment

# # cleaned_food.csv
# # airbnb = intersection_airbnb
# airbnb = pd.read_csv('intermediate_scores/airbnb_e.csv')
# amen_intersection, name = inters.amentiy_intersections('cleaned_food.csv')
# intersection_airbnb = inters.intersection_score(airbnb, amen_intersection, name)
# intersection_airbnb.to_csv('airbnb_e' + name[0] +'.csv', index=False) # -> airbnb_ef.csv with entertainment,food

# # cleaned_leisure.csv
# # airbnb = intersection_airbnb
# airbnb = pd.read_csv('intermediate_scores/airbnb_ef.csv')
# amen_intersection, name = inters.amentiy_intersections('cleaned_leisure.csv')
# intersection_airbnb = inters.intersection_score(airbnb, amen_intersection, name)
# intersection_airbnb.to_csv('airbnb_ef' + name[0] +'.csv', index=False) # -> airbnb_food.csv with entertainment,food,leisure

# # cleaned_transportation.csv
# # airbnb = intersection_airbnb
# airbnb = pd.read_csv('intermediate_scores/airbnb_efl.csv')
# amen_intersection, name = inters.amentiy_intersections('cleaned_transportation.csv')
# intersection_airbnb = inters.intersection_score(airbnb, amen_intersection, name)
# intersection_airbnb.to_csv('airbnb_efl' + name[0] +'.csv', index=False) # -> airbnb_food.csv with entertainment,food,leisure,transportation

# # cleaned_shop.csv
# # airbnb = intersection_airbnb
# airbnb = pd.read_csv('intermediate_scores/airbnb_eflt.csv')
# amen_intersection, name = inters.amentiy_intersections('cleaned_shop.csv')
# intersection_airbnb = inters.intersection_score(airbnb, amen_intersection, name)
# intersection_airbnb.to_csv('airbnb_eflt' + name[0] +'.csv', index=False) # -> airbnb_food.csv with entertainment,food,leisure,transportation,shop

# cleaned_tourism.csv
# airbnb = intersection_airbnb
# airbnb = pd.read_csv('intermediate_scores/airbnb_eflts.csv')
# amen_intersection, name = inters.amentiy_intersections('cleaned_tourism.csv')
# intersection_airbnb = inters.intersection_score(airbnb, amen_intersection, name)
# intersection_airbnb.to_csv('airbnb_score.csv', index=False) # -> airbnb_food.csv with entertainment,food,leisure,transportation,shop,tourism

# %%
