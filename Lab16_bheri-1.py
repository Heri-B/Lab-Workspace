"""
Lab 16
Bekhit Heri
12/15/25

This program reads the unemployment rates from 1975 to 2025.
"""

from pathlib import Path
from datetime import datetime
import matplotlib.pyplot as plt

path = Path('UNRATE.csv')
lines = path.read_text(encoding='utf-8').splitlines()

header = lines[0].split(',')
print("CSV Header Information:")
for index, column in enumerate(header):
    print(f"{index}: {column}")

dates = []
rates = []

for line in lines[1:]:
    columns = line.split(',')
    date = datetime.strptime(columns[0], "%Y-%m-%d")
    rate = float(columns[1])

    dates.append(date)
    rates.append(rate)

plt.style.use('seaborn-v0_8')

fig, ax = plt.subplots(figsize=(10, 7))
ax.plot(dates, rates, color='blue')

ax.set_title("U.S. Unemployment Rate (1975–2025)", fontsize=24)
ax.set_xlabel('Year', fontsize=16)
ax.set_ylabel("Unemployment Rate (%)", fontsize=16)
ax.tick_params(labelsize=16)

plt.gcf().autofmt_xdate()
plt.show()