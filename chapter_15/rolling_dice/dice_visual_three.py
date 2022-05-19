from plotly import offline
from die import Die
from plotly.graph_objs import Bar, Layout
# 创建三个 D6 骰子。
die_1 = Die()
die_2 = Die()
die_3 = Die()

# 掷骰子多次，并将结果存储在一个列表中。
results = [die_1.roll() + die_2.roll() + die_3.roll() for roll_num in range(1_000_000)]

# 分析结果。
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
frequencies = [results.count(value) for value in range(3, max_result+1)]

# 可视化结果。
x_values = list(range(3, max_result+1))
data = [Bar(x=x_values, y=frequencies)]
x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling three D6 dice 1,000,000 times',
xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='3d6.html')