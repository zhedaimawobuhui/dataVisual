from plotly import offline
from plotly.graph_objs import Densitymapbox, Layout
import pandas as pd

filename = "data/world_fires_1_day.csv"

datas = pd.read_csv(filename)

data = [Densitymapbox(lat=datas["latitude"], lon=datas["longitude"], z=datas["scan"], radius=4)]
my_layout = Layout(title='全球地震散点图',
          mapbox_style = 'open-street-map'
)

offline.plot({'data': data, 'layout': my_layout}, filename='3d6.html')