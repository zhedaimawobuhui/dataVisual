import csv
from datetime import datetime
import pandas as pd
from matplotlib import pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'

# 读取文件
data = pd.read_csv(filename,parse_dates = ['DATE'])

# # 绘制高温和低温。
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(data["DATE"], data["TMAX"], c='red')

# 格式化绘图。
plt.title("Daily high temperatures - 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()