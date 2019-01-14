import plotly
import plotly.graph_objs as go

def graph_01():
    filename = "images/a.html"
    plot_obj = plotly.offline.plot({
                "data": [go.Scatter(x=[1, 2, 3, 4], y=[4, 3, 2, 1])],
                "layout": go.Layout(title="hello world"),
               },filename=filename, auto_open=False, output_type="div")

    return plot_obj

if __name__ == "__main__":
    graph_01()