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

    locator = []
    diagnostic0 = []
    diagnostic1 = []
    diagnostic2 = []
    diagnostic3 = []
    diagnostic4 = []
    diagnostic5 = []
    for i in a['data.locator'].unique():
        res = a[a['data.locator'] == i]['data.diagnostic']
        locator.append(i)
        diagnostic0.append(res[res == 0].count())
        diagnostic1.append(res[res == 1].count())
        diagnostic2.append(res[res == 2].count())
        diagnostic3.append(res[res == 3].count())
        diagnostic4.append(res[res == 4].count())
        diagnostic5.append(res[res == 5].count())

    df = pd.DataFrame({'data.locator': locator, 'diagnostic0': diagnostic0, 'diagnostic1': diagnostic1,
                       'diagnostic2': diagnostic2, 'diagnostic3': diagnostic3, 'diagnostic4': diagnostic4,
                       'diagnostic5': diagnostic5})
    geo_loc_df_summary = nomi.query_postal_code(df['data.locator'].tolist())
    df_out_summary = df.join(geo_loc_df_summary)

    df_out = a.join(geo_loc_df)
    json_out = df_out.to_json(orient="records")
    json_out_summary = df_out_summary.to_json(orient="records")
    return json_out, df_out, json_out_summary, df_out_summary
