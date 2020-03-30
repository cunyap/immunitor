import json
import os
import pandas as pd
import pgeocode


def get_data_from_json():

    directory = os.getcwd() + '/app/raw-data'
    cnt = 0
    for filename in os.listdir(directory):
        if filename.endswith(".json") and cnt == 0:
            with open(os.path.join(directory, filename)) as json_file:
                d_temp = json.load(json_file)
                data = d_temp
                cnt += 1
            continue
        elif filename.endswith(".json"):
            with open(os.path.join(directory, filename)) as json_file:
                 d_temp = json.load(json_file)
                 data = data + d_temp
                 cnt += 1
            continue
        else:
            print('none')

    a = pd.io.json.json_normalize(data)

    # Unique zip codes
    # a['data.locator'].unique()

    nomi = pgeocode.Nominatim('ch')
    geo_loc_df = nomi.query_postal_code(a['data.locator'].tolist())

    df_out = a.join(geo_loc_df)
    json_out = df_out.to_json(orient="records")
    return json_out, df_out
