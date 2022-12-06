#%%
import pandas as pd
import numpy as np

df = pd.read_json(
    "output/shop/shop.json.gz", lines=True, compression="gzip"
)
#%%
df['type'].unique()

# # array(['bicycle', 'supermarket', 'books', 'cannabis', 'alcohol',
#        'convenience', 'toys', 'art', 'sports', 'dry_cleaning', 'bakery',
#        'stationery', 'baby_goods', 'clothes', 'outdoor', 'hairdresser',
#        'locksmith', 'erotic', 'craft', 'electronics', 'bed', 'tailor',
#        'ice_cream', 'second_hand', 'furniture', 'florist', 'paint',
#        'gift', 'mobile_phone', 'tea', 'car_repair', 'chemist',
#        'department_store', 'hifi', 'nutrition_supplements', 'optician',
#        'pet', 'greengrocer', 'tattoo', 'camera', 'motorcycle', 'shoes',
#        'car', 'confectionery', 'butcher', 'seafood', 'laundry',
#        'patisserie', 'yes', 'kitchen', 'wine', 'art_supplies',
#        'musical_instrument', 'computer', 'interior_decoration',
#        'beverages', 'spices', 'deli', 'market', 'funeral_directors',
#        'estate_agent', 'newsagent', 'massage', 'beauty', 'cosmetics',
#        'jewelry', 'wool', 'hardware', 'boat', 'money_lender',
#        'motorcycle_repair', 'insurance', 'doityourself', 'charity',
#        'hearing_aids', 'model', 'bag', 'photo', 'flooring',
#        'swimming_pool', 'coffee', 'tobacco', 'discount', 'video', 'Signs',
#        'hobby', 'storage_rental', 'pawnbroker', 'food', 'honey',
#        'pet_supply', 'print', 'copyshop', 'variety_store', 'frame',
#        'car_parts', 'tool_hire', 'travel_agency', 'herbalist',
#        'pet_grooming', 'music', 'fabric', 'tyres', 'wholesale',
#        'antiques', 'hairdresser_supply', 'e-cigarette', 'vacant',
#        'bedding', 'chocolate', 'health_food', 'carpet', 'pastry',
#        'ticket', 'bulk', 'printing', 'religion', 'houseware', 'watches',
#        'fashion_accessories', 'video_games', 'bookmaker',
#        'kitchenware;clothes', 'boutique', 'appliance', 'medical_supply',
#        'grocery', 'rental', "Kid's_clothing", 'radiotechnics', 'leather',
#        'scuba_diving', 'games', 'sewing', 'psilocybin', 'collector',
#        'optics', 'electrical', 'curtain', 'trade', 'lighting',
#        'shoe_repair', 'military_surplus', 'cheese', 'comics', 'agrarian',
#        'bathroom_furnishing', 'fireplace;hvac', 'used', 'garden_centre',
#        'tool_repair', 'fitness', 'greengrocer;garden_centre',
#        'vacuum_cleaner', 'hydroponics', 'fireplace', 'tiles', 'flag',
#        'orthotics', 'wigs', 'party', 'condo', 'glass', 'inkjet',
#        'frozen_food', 'auction_house', 'roofing', 'repair', 'hat',
#        'stamp', 'pump', 'general', 'perfumery', 'lottery', 'water',
#        'dentures'], dtype=object)

# TODO: Keep
# 'supermarket', 'cannabis', 'convenience', 
# 'art', 'sports', 'alcohol', 'bakery', 'stationery', 
# 'clothes', 'outdoor', 'erotic', 'craft', 'electronics', 
# 'second_hand',  'gift', 'department_store',  'nutrition_supplements', 
# 'camera', 'shoes', 'confectionery', 'butcher', 'seafood', 
# 'patisserie', 'general', 'wine', 'beauty', 'e-cigarette', 'variety_store', 
# 'beverages', 'spices', 'tea', 'market', 'wholesale', 'newsagent', 'chemist', 'cosmetics', 
# 'jewelry', 'charity', 'bag', 'photo', 'food', 'tobacco', 'cheese', 'discount', 
# 'hobby', 'honey', 'ice_cream', 'medical_supply', 'chocolate', 'antiques', 
# 'health_food', 'coffee', 'fashion', 'pastry', 'ticket', 'bulk', 'watches', 
# 'fashion_accessories', 'boutique', 'grocery', 'rental', "Kid's_clothing", 
# 'scuba_diving', 'psilocybin', 'collector', 'used', 'greengrocer;garden_centre', 
# 'party', 'frozen_food', 'hat', 'perfumery'

#%%
# https://towardsdatascience.com/all-pandas-json-normalize-you-should-know-for-flattening-json-13eae1dfb7dd
# print(amenities)
# print(amenities['amenity'].unique())
tags = pd.json_normalize(df["tags"])
unnested_df= pd.concat([df, tags], axis=1)

count = unnested_df.groupby(['type'])['type'].count()

# type
# Kid's_clothing      1
# Signs               1
# agrarian            1
# alcohol           112
# antiques            5
#                  ... 
# wholesale          11
# wigs                1
# wine                7
# wool                2
# yes                48
# Name: type, Length: 176, dtype: int64

#%%
shop_condition = (
    (df['type'] == 'supermarket') |
    (df['type'] == 'cannabis') |
    (df['type'] == 'convenience') |
    (df['type'] == 'art') |
    (df['type'] == 'sports') |
    (df['type'] == 'alcohol') |
    (df['type'] == 'bakery') |
    (df['type'] == 'stationery') |
    (df['type'] == 'clothes') |
    (df['type'] == 'outdoor') |
    (df['type'] == 'erotic') |
    (df['type'] == 'craft') |
    (df['type'] == 'electronics') |
    (df['type'] == 'second_hand') |
    (df['type'] == 'gift') |
    (df['type'] == 'department_store') |
    (df['type'] == 'nutrition_supplements') |
    (df['type'] == 'camera') |
    (df['type'] == 'shoes') |
    (df['type'] == 'confectionery') |
    (df['type'] == 'butcher') |
    (df['type'] == 'seafood') |
    (df['type'] == 'patisserie') |
    (df['type'] == 'general') |
    (df['type'] == 'wine') |
    (df['type'] == 'beauty') |
    (df['type'] == 'e-cigarette') |
    (df['type'] == 'variety_store') |
    (df['type'] == 'beverages') |
    (df['type'] == 'spices') |
    (df['type'] == 'tea') |
    (df['type'] == 'market') |
    (df['type'] == 'wholesale') |
    (df['type'] == 'newsagent') |
    (df['type'] == 'chemist') |
    (df['type'] == 'cosmetics') |
    (df['type'] == 'jewelry') |
    (df['type'] == 'charity') |
    (df['type'] == 'bag') |
    (df['type'] == 'photo') |
    (df['type'] == 'food') |
    (df['type'] == 'tobacco') |
    (df['type'] == 'cheese') |
    (df['type'] == 'discount') |
    (df['type'] == 'hobby') |
    (df['type'] == 'honey') |
    (df['type'] == 'ice_cream') |
    (df['type'] == 'medical_supply') |
    (df['type'] == 'chocolate') |
    (df['type'] == 'antiques') |
    (df['type'] == 'health_food') |
    (df['type'] == 'coffee') |
    (df['type'] == 'fashion') |
    (df['type'] == 'pastry') |
    (df['type'] == 'ticket') |
    (df['type'] == 'bulk') |
    (df['type'] == 'watches') |
    (df['type'] == 'fashion_accessories') |
    (df['type'] == 'boutique') |
    (df['type'] == 'grocery') |
    (df['type'] == 'rental') |
    (df['type'] == "Kid's_clothing") |
    (df['type'] == 'scuba_diving') |
    (df['type'] == 'psilocybin') |
    (df['type'] == 'collector') |
    (df['type'] == 'used') |
    (df['type'] == 'greengrocer;garden_centre') |
    (df['type'] == 'party') |
    (df['type'] == 'frozen_food') |
    (df['type'] == 'hat') |
    (df['type'] == 'perfumery')
)

#%%
shop_df = df[shop_condition]

#%%
shop_df.to_csv("cleaned_shop_amenities.csv", index=False)
# %%