import json
import plotly
import plotly.graph_objects as go


def create_plot(df):
    sel_geo_region = df['state_name']
    diagnostic = df['data.diagnostic']
    cond0 = df['data.diagnostic'] == 0
    cond1 = df['data.diagnostic'] == 1
    cond2 = df['data.diagnostic'] == 2
    cond3 = df['data.diagnostic'] == 3
    cond4 = df['data.diagnostic'] == 4

    data_dict = dict( data = [
               go.Bar(
                   name="Negative",
                   x=sel_geo_region[cond0],
                   y=diagnostic[cond0] + 1,
                   offsetgroup=5,
               ),
               go.Bar(
                   name="Model 1",
                   x=sel_geo_region[cond1],
                   y=diagnostic[cond1],
                   offsetgroup=1,
               ),
               go.Bar(
                   name="Model 2",
                   x=sel_geo_region[cond2],
                   y=diagnostic[cond2],
                   offsetgroup=2,
               ),
               go.Bar(
                   name="Model 3",
                   x=sel_geo_region[cond3],
                   y=diagnostic[cond3],
                   offsetgroup=3,
               ),
               go.Bar(
                   name="Recovered",
                   x=sel_geo_region[cond4],
                   y=diagnostic[cond4],
                   offsetgroup=4,
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
