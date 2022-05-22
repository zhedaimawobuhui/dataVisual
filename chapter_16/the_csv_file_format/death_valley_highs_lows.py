import csv
from datetime import datetime
import pandas as pd
from matplotlib import pyplot as plt

filename = 'data/death_valley_2018_simple.csv'

# 读文件
data = pd.read_csv(filename,error_bad_lines=False,parse_dates = ['DATE'])

# 传入数据
dates = data["DATE"]
highs = data["TMAX"]
lows = data["TMIN"]

# with open(filename) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
#
#     # Get dates, and high and low temperatures from this file.
#     dates, highs, lows = [], [], []
#     for row in reader:
#         current_date = datetime.strptime(row[2], '%Y-%m-%d')
#         try:
#             high = int(row[4])
#             low = int(row[5])
#         except ValueError:
#             print(f"Missing data for {current_date}")
#         else:
#             dates.append(current_date)
#             highs.append(high)
#             lows.append(low)

# Plot the high and low temperatures.
# 传入数据，画出曲线
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
# 设置图像格式
title = "Daily high and low temperatures - 2018\nDeath Valley, CA"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()