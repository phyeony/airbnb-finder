import sys
import pandas as pd

# load
stops = pd.read_csv('Stops-with-boundary.csv')
stations = pd.read_csv('Stations-with-boundary.csv')

# load boundaries
boundary= pd.read_csv('boundary.csv')
boundary_list = boundary['name']

# count all the stops/stations for each boundary
stop_counts = stops.groupby(['boundary'])['stop_name'].count()
station_counts = stations.groupby(['boundary'])['Exch_Name'].count()

# merge two count lists
data = {'stops': stop_counts, 'stations': station_counts}
counts = pd.DataFrame(data=data, index=boundary_list)
counts['stations'] = counts['stations'].fillna(0)
counts['stations'] = counts['stations'].apply(lambda x: int(x))

# export
counts.to_csv('counts.csv', index=True)