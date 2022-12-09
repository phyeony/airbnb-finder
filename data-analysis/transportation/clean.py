#%%
import pandas as pd

stop = pd.read_csv("Stops.csv")
station = pd.read_csv("Stations.csv")

stop = stop[['stop_name','Longitude','Latitude']]
station = station[['Exch_Name','Longitude','Latitude']]

stop.rename(columns={'stop_name': 'name'}, inplace=True)
station.rename(columns={'Exch_Name': 'name'}, inplace=True)
combined = pd.concat([stop, station], axis=0)

combined.to_csv("cleaned_public_transportation.csv")
# %%
