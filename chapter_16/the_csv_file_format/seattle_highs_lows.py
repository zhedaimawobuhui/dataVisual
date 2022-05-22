import pandas as pd
from matplotlib import pyplot as plt

filename = 'data/2016-weather-data-seattle.csv'
# 读文件
data = pd.read_csv(filename,parse_dates = ['Date'])

# 传入数据
dates = data["Date"]
highs = data["Max_TemperatureC"]
lows = data["Min_TemperatureC"]

# Plot the high and low temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
plt.title("2015 seattle high and low temperatures - 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()