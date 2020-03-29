import pgeocode
nomi = pgeocode.Nominatim('ch')
print(nomi.query_postal_code("5430"))

geodata_collection = {"geometry": {"type": "Point", "coordinates": [125.6, 10.1]}}
print(geodata_collection['geometry']['coordinates'])
print(geodata_collection.get('coordinates'))
for geo_feature in geodata_collection:
    print(geo_feature)
    print('bla')



import json
from flask import jsonify

with open('raw-data/data-2020-03-24T23_2020-03-25T00.json') as json_file:
    data = json.load(json_file)

    import pandas as pd

    # converting json dataset from dictionary to dataframe
    train = pd.DataFrame.from_dict(data[0], orient='index')
    train.reset_index(level=0, inplace=True)
    print(pd.io.json.json_normalize(data))