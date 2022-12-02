#%%
import pandas as pd

df = pd.read_json(
    "output/shop/shop.json.gz", lines=True, compression="gzip"
)
#%%
df['type'].unique()

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

# TODO: Delete unnecessary types 
# yes, supermarket, truck, ...


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
# unnested_df.to_csv("cleaned_shop_amenities.csv", index=False)