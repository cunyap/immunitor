import json
import plotly
import plotly.graph_objects as go
import plotly.express as px


def create_plot(df):
    sel_geo_region = df['state_name']
    diagnostic = df['data.diagnostic']
    cond0 = df['data.diagnostic'] == 0
    cond1 = df['data.diagnostic'] == 1
    cond2 = df['data.diagnostic'] == 2
    cond3 = df['data.diagnostic'] == 3
    cond4 = df['data.diagnostic'] == 4
    cond5 = df['data.diagnostic'] == 5

    data_dict = dict( data = [
        go.Bar(
            name="healthy",
            x=sel_geo_region[cond0],
            y=diagnostic[cond0] + 1,
            marker=dict(color='rgb(17,205,239)'),
            offsetgroup=6,
        ),
        go.Bar(
            name="sick (other disease)",
            x=sel_geo_region[cond1],
            y=diagnostic[cond1],
            marker=dict(color='rgb(17,205,239)'),
            offsetgroup=1,
        ),
        go.Bar(
            name="sick (probably covid19)",
            x=sel_geo_region[cond2],
            y=diagnostic[cond2],
            marker=dict(color='rgb(251,99,64)'),
            offsetgroup=2,
        ),
        go.Bar(
            name="sick (covid19 confirmed)",
            x=sel_geo_region[cond3],
            y=diagnostic[cond3],
            marker=dict(color='rgb(245,54,92)'),
            offsetgroup=3,
        ),
        go.Bar(
            name="recovered (not confirmed)",
            x=sel_geo_region[cond4],
            y=diagnostic[cond4],
            marker=dict(color='rgb(45,206,137)'),
            offsetgroup=4,
        ),
        go.Bar(
            name="recovered (confirmed)",
            x=sel_geo_region[cond5],
            y=diagnostic[cond5],
            marker=dict(color='rgb(45,206,137)'),
            offsetgroup=5,
        )
    ],
        layout = go.Layout(
            title="Reported Covid19 test cases",
            yaxis_title="Number of test cases",
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)'
        ))
    graphJSON = json.dumps(data_dict, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON
