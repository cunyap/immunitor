import os
import pandas as pd
from pybis import Openbis


def establish_db_connection():

    # Should be done during server startup or when calling a function to set or get data
    o = Openbis(os.environ['OPENBIS_SERVER'], verify_certificates=False)
    o.login(os.environ['OPENBIS_USER'], os.environ['OPENBIS_PASSWORD'])
    return o


def register_new_case(o, data):

    sample = o.new_sample(
        type='CASE',
        space='DEFAULT',
        experiment='/DEFAULT/COVID19/E1',
        props=data,
        parents=[],
        children=[])
    sample.save()

    return sample.permId


def update_case(o, data):

    parent = o.get_sample('20170518112808649-52')  # we need to get this number from the user, should be in data
    sample = o.new_sample(
        type='CASE',
        space='DEFAULT',
        experiment='/DEFAULT/COVID19/E1',
        props=data,
        parents=[parent],
        children=[])
    sample.save()

    return sample.permId


def get_all_cases(o):

    samples = o.get_samples(space='DEFAULT/COVID19', experiment='/DEFAULT/COVID19/E1')
    samples_as_json = pd.io.json.json_normalize(samples.df)

    return samples_as_json, samples.df
