import pandas as pd

df = pd.read_json('local-area-boundary.json')
fields = df['fields']

name = pd.Series(fields.apply(lambda x: x['name']), name="name")
ID = pd.Series(fields.apply(lambda x: x['mapid']), name="ID")
coord = pd.Series(fields.apply(lambda x: x['geom']['coordinates']), name="coordinates")

boundary = pd.concat([name,ID,coord],axis=1)

boundary.to_csv('boundary.csv', index=False)
