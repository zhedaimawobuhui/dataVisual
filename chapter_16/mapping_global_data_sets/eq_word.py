from plotly import offline
from plotly.graph_objs import Densitymapbox, Layout
import pandas as pd

filename = "data/world_fires_1_day.csv"
# 读取文件
datas = pd.read_csv(filename)
# 标散点
data = [Densitymapbox(lat=datas["latitude"], lon=datas["longitude"], z=datas["scan"], radius=4)]
# 设置图形样式
my_layout = Layout(title='全球地震散点图',
          mapbox_style = 'open-street-map'
)
# 输出图形
offline.plot({'data': data, 'layout': my_layout}, filename='3d6.html')