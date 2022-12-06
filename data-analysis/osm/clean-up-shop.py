#%%
import pandas as pd
import numpy as np

df = pd.read_json(
    "output/shop/shop.json.gz", lines=True, compression="gzip"
)
#%%
# df['type'].unique()

# array(['bicycle', 'supermarket', 'tyres', 'video', 'books', 'cannabis',
#        'convenience', 'toys', 'art', 'sports', 'dry_cleaning', 'alcohol',
#        'bakery', 'stationery', 'baby_goods', 'clothes', 'outdoor',
#        'hairdresser', 'locksmith', 'erotic', 'craft', 'electronics',
#        'bed', 'tailor', 'second_hand', 'furniture', 'florist', 'paint',
#        'gift', 'mobile_phone', 'car_repair', 'department_store', 'hifi',
#        'nutrition_supplements', 'optician', 'pet', 'greengrocer',
#        'tattoo', 'camera', 'motorcycle', 'shoes', 'car', 'confectionery',
#        'butcher', 'seafood', 'laundry', 'patisserie', 'general', 'yes',
#        'kitchen', 'liquor', 'wine', 'art_supplies', 'musical_instrument',
#        'beauty', 'copyshop', 'hearing_aids', 'money_lender',
#        'e-cigarette', 'variety_store', 'estate_agent', 'massage',
#        'vacuum_cleaner', 'computer', 'interior_decoration', 'beverages',
#        'spices', 'deli', 'tea', 'market', 'wholesale',
#        'funeral_directors', 'newsagent', 'chemist', 'cosmetics',
#        'jewelry', 'garden_centre', 'doityourself', 'wool', 'hardware',
#        'boat', 'storage_rental', 'motorcycle_repair', 'insurance',
#        'car_parts', 'charity', 'model', 'bag', 'photo', 'shoe_repair',
#        'flooring', 'food', 'lighting', 'houseware', 'fabric', 'appliance',
#        'cash', 'swimming_pool', 'tobacco', 'vacant', 'pottery', 'cheese',
#        'discount', 'video_games', 'pawnbroker', 'music', 'Signs', 'hobby',
#        'honey', 'pet_supply', 'print', 'frame', 'ice_cream', 'tool_hire',
#        'medical_supply', 'chocolate', 'travel_agency', 'herbalist',
#        'pet_grooming', 'carpet', 'antiques', 'hairdresser_supply',
#        'bedding', 'health_food', 'coffee', 'fashion', 'pastry', 'ticket',
#        'bulk', 'printing', 'religion', 'watches', 'fashion_accessories',
#        'bookmaker', 'kitchenware;clothes', 'boutique', 'radiotechnics',
#        'grocery', 'rental', "Kid's_clothing", 'leather', 'scuba_diving',
#        'games', 'sewing', 'lottery', 'psilocybin', 'collector', 'optics',
#        'electrical', 'curtain', 'trade', 'military_surplus', 'doors',
#        'comics', 'agrarian', 'bathroom_furnishing', 'Plumbing',
#        'office_supplies', 'fireplace;hvac', 'used', 'tool_repair',
#        'fitness', 'bar_supplies', 'sanitary', 'uniforms', 'coffins',
#        'electronic_repair', 'construction_equipment',
#        'construction_supplies', 'packaging', 'industrial', 'psychic',
#        'greengrocer;garden_centre', 'trophy', 'mobility_scooter',
#        'surveillance', 'hydroponics', 'fireplace', 'tiles',
#        'brewing_supplies', 'flag', 'orthotics', 'wigs', 'party', 'hvac',
#        'supplements', 'condo', 'glass', 'inkjet', 'frozen_food',
#        'auction_house', 'garden_furniture', 'power_equipment',
#        'printer_ink', 'window_blind', 'rubber_stamps', 'security',
#        'copier', 'metal', 'roofing', 'industrial_supplies', 'power_tools',
#        'repair', 'hat', 'stamp', 'truck', 'pump', 'fishing', 'perfumery',
#        'water', 'dentures'], dtype=object)

# TODO: Keep
# 'supermarket', 'cannabis', 'convenience', 
# 'art', 'sports', 'alcohol', 'bakery', 'stationery', 
# 'clothes', 'outdoor', 'erotic', 'craft', 'electronics', 
# 'second_hand',  'gift', 'department_store',  'nutrition_supplements', 
# 'greengrocer', 'camera', 'shoes', 'confectionery', 'butcher', 'seafood', 
# 'patisserie', 'general', 'liquor', 'wine', 'beauty', 'e-cigarette', 'variety_store', 
# 'beverages', 'spices', 'tea', 'market', 'wholesale', 'newsagent', 'chemist', 'cosmetics', 
# 'jewelry', 'charity', 'bag', 'photo', 'food', 'tobacco', 'cheese', 'discount', 
# 'hobby', 'honey', 'ice_cream', 'medical_supply', 'chocolate', 'antiques', 
# 'health_food', 'coffee', 'fashion', 'pastry', 'ticket', 'bulk', 'watches', 
# 'fashion_accessories', 'boutique', 'grocery', 'rental', "Kid's_clothing", 
# 'scuba_diving', 'psilocybin', 'collector', 'used', 'greengrocer;garden_centre', 
# 'party', 'supplements', 'frozen_food', 'hat', 'fishing', 'perfumery'

#%%
# https://towardsdatascience.com/all-pandas-json-normalize-you-should-know-for-flattening-json-13eae1dfb7dd
# print(amenities)
# print(amenities['amenity'].unique())
tags = pd.json_normalize(df["tags"])
unnested_df= pd.concat([df, tags], axis=1)

count = unnested_df.groupby(['type'])['type'].count()

# type
# Kid's_clothing      1
# Plumbing            1
# Signs               1
# agrarian            1
# alcohol           130
#                  ... 
# wigs                1
# window_blind        1
# wine                9
# wool                2
# yes                56
# Name: type, Length: 211, dtype: int64

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
    (df['type'] == 'greengrocer') |
    (df['type'] == 'camera') |
    (df['type'] == 'shoes') |
    (df['type'] == 'confectionery') |
    (df['type'] == 'butcher') |
    (df['type'] == 'seafood') |
    (df['type'] == 'patisserie') |
    (df['type'] == 'general') |
    (df['type'] == 'liquor') |
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
    (df['type'] == 'supplements') |
    (df['type'] == 'frozen_food') |
    (df['type'] == 'hat') |
    (df['type'] == 'fishing') |
    (df['type'] == 'perfumery')
)

#%%
shop_df = df[shop_condition]

#%%
shop_df.to_csv("cleaned_shop_amenities.csv", index=False)
# %%