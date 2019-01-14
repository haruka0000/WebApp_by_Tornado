import plotly
import plotly.graph_objs as go

def graph_01():
    plot_obj = plotly.offline.plot({
                "data": [go.Scatter(x=[1, 2, 3, 4], y=[4, 5, 2, 8])],
                "layout": go.Layout(title="hello world"),
               }, auto_open=False, output_type="div")

    return plot_obj

