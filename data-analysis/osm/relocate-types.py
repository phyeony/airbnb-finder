#%%
import pandas as pd

# from entertainment file, move marketplace, arts_centre types to tourism file
entertainment = pd.read_csv("cleaned_entertainment.csv")

# select
marketplace = entertainment[entertainment["type"] == "marketplace"]
arts_centre = entertainment[entertainment["type"] == "arts_centre"]
spa = entertainment[entertainment["type"] == "spa"]

# drop
entertainment = entertainment.drop(entertainment[entertainment["type"] == "marketplace"].index)
entertainment = entertainment.drop(entertainment[entertainment["type"] == "arts_centre"].index)
entertainment = entertainment.drop(entertainment[entertainment["type"] == "spa"].index)

# save entertainment
entertainment.to_csv("cleaned_entertainment.csv", index=False)

# save tourism 
tourism = pd.read_csv("cleaned_tourism.csv")
tourism = tourism.append(marketplace)
tourism = tourism.append(arts_centre)
tourism.to_csv("cleaned_tourism.csv", index=False)

# save leisure
leisure = pd.read_csv("cleaned_leisure.csv")
leisure = leisure.append(spa)
leisure.to_csv("cleaned_leisure.csv", index=False)
# %%
