import pandas as pd

#import
df = pd.read_json('local-area-boundary.json')
fields = df['fields']

# refactor columns
name = pd.Series(fields.apply(lambda x: x['name']), name="name")
ID = pd.Series(fields.apply(lambda x: x['mapid']), name="ID")
coord = pd.Series(fields.apply(lambda x: x['geom']['coordinates'][0]), name="coordinates")
# concatenate together
boundary = pd.concat([name,ID,coord],axis=1) 

# export
boundary.to_csv('boundary.csv', index=False)
