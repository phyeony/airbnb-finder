import pandas as pd

stop = pd.read_csv("Stops.csv")
station = pd.read_csv("Stations.csv")

del stop['x'], stop['y']
del station['x'], station['y']

stop.to_csv('cleaned_stops.csv')
station.to_csv('cleaned_stations.csv')