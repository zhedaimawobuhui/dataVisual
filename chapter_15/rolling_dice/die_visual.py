from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# 创建一个 D6。
die = Die()

# 做一些投掷，并将结果存储在列表中。
results = [die.roll() for roll_num in range(1000)]

# 分析结果
frequencies = [results.count(value) for value in range(1, die.num_sides+1)]

# 可视化结果
x_values = list(range(1, die.num_sides+1))
#画线
data = [Bar(x=x_values, y=frequencies)]

# 设置图形样式
x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling one D6 1000 times',
        xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')
