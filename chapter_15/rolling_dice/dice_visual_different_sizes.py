from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# 创建一个 D6 和一个 D10
die_1 = Die()
die_2 = Die(10)

# 做一些投掷，并将结果存储在列表中。
results = [die_1.roll() + die_2.roll() for roll_num in range(50_000)]

    
# 分析结果
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result+1)]

    
# 可视化结果
x_values = list(range(2, max_result+1))

#画线
data = [Bar(x=x_values, y=frequencies)]

#设置图形样式
x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling a D6 and a D10 50000 times',
        xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d10.html')