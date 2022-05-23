from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# 创建两个 D6 骰子。
die_1 = Die()
die_2 = Die()

# 做一些投掷，并将结果存储在列表中。
results = [die_1.roll() + die_2.roll() for roll_num in range(1000)]

    
# 分析结果
max_result = die_1.num_sides + die_2.num_sides
frequencies = [ results.count(value) for value in range(2, max_result+1)]

    
# 将结果可视化
x_values = list(range(2, max_result+1))
# 画线
data = [Bar(x=x_values, y=frequencies)]

# 设置图象信息
x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling two D6 dice 1000 times',
        xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6.html')