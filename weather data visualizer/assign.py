# ---------------------------------------------
# WEATHER DATA VISUALIZER - MINI PROJECT
# BY: TUSHAR CHAND
# ROLL NO:2501410053
# ---------------------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -------------------------------
# TASK 1: DATA LOADING
# -------------------------------

# Load the dataset (replace with your file name)
df = pd.read_csv("weather_data.csv")

print("----- Dataset Head -----")
print(df.head())

print("\n----- Dataset Info -----")
print(df.info())

print("\n----- Dataset Summary -----")
print(df.describe())


# -------------------------------
# TASK 2: DATA CLEANING
# -------------------------------

# Convert date column to datetime
df['date'] = pd.to_datetime(df['date'])

# Handling missing values
df = df.dropna()   # or df.fillna(method='ffill')

# Select important columns
df = df[['date', 'temperature', 'humidity', 'rainfall']]

# Save cleaned data
df.to_csv("cleaned_weather_data.csv", index=False)


# -------------------------------
# TASK 3: STATISTICAL ANALYSIS
# -------------------------------

# Daily statistics
daily_mean_temp = df['temperature'].mean()
daily_min_temp = df['temperature'].min()
daily_max_temp = df['temperature'].max()
daily_std_temp = df['temperature'].std()

print("\n----- Daily Temperature Stats -----")
print("Mean Temperature:", daily_mean_temp)
print("Min Temperature:", daily_min_temp)
print("Max Temperature:", daily_max_temp)
print("Standard Deviation:", daily_std_temp)

# Monthly grouping
df['month'] = df['date'].dt.month
monthly_rainfall = df.groupby('month')['rainfall'].sum()
monthly_temp = df.groupby('month')['temperature'].mean()


# -------------------------------
# TASK 4: VISUALIZATION
# -------------------------------

# 1. Line Chart - Daily Temperature Trend
plt.figure(figsize=(10,5))
plt.plot(df['date'], df['temperature'])
plt.title("Daily Temperature Trend")
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.savefig("temperature_trend.png")
plt.show()

# 2. Bar Chart - Monthly Rainfall
plt.figure(figsize=(10,5))
plt.bar(monthly_rainfall.index, monthly_rainfall.values)
plt.title("Monthly Rainfall")
plt.xlabel("Month")
plt.ylabel("Rainfall")
plt.savefig("monthly_rainfall.png")
plt.show()

# 3. Scatter Plot - Humidity vs Temperature
plt.figure(figsize=(8,5))
plt.scatter(df['temperature'], df['humidity'])
plt.title("Humidity vs Temperature")
plt.xlabel("Temperature")
plt.ylabel("Humidity")
plt.savefig("humidity_vs_temp.png")
plt.show()

# 4. Combined Plot (Subplots)
plt.figure(figsize=(12,8))

plt.subplot(2,1,1)
plt.plot(df['date'], df['temperature'], label="Temperature")
plt.title("Temperature Over Time")

plt.subplot(2,1,2)
plt.scatter(df['temperature'], df['humidity'], color='red')
plt.title("Humidity vs Temperature")

plt.tight_layout()
plt.savefig("combined_plot.png")
plt.show()


# -------------------------------
# TASK 5: GROUPING & AGGREGATION
# -------------------------------

seasonal_data = df.groupby(df['date'].dt.quarter).mean()

print("\n----- Seasonal Averages -----")
print(seasonal_data)


# -------------------------------
# TASK 6: EXPORTING RESULTS
# -------------------------------

df.to_csv("final_cleaned_weather.csv", index=False)
print("\nAll files exported successfully!")
