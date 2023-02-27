import pandas as pd
import numpy as np
import seaborn as sns
import statsmodels
import matplotlib.pyplot as plt
import math
import codecademylib3


## Read in Data
flight = pd.read_csv("flight.csv")
print(flight.head())

## Task 1
#sns.histplot(data=flight, x='coach_price', binwidth = 10)
#plt.show()
#plt.clf()

#print('Coach price mean:\n', flight['coach_price'].mean())
#print('Coach price median:\n', flight['coach_price'].median())

# $500 is too pricy for a coach price 

## Task 2
#sns.histplot(data=flight, x=flight.coach_price[flight.hours==8])
#plt.show()
#plt.clf()

mean_8 = np.mean(flight.coach_price[flight.hours == 8])
#print('Mean 8 hours flight:', mean_8)
median_8 = np.median(flight.coach_price[flight.hours == 8])
#print('Median 8 hours flight:', median_8)

## $500 is closer to the mean
# $500 seems reasonable for an 8 hours flight

## Task 3
#print(flight['delay'].value_counts())
#sns.histplot(data=flight, x=flight.delay[flight.delay<= 100], bins = 20)
#plt.show()
#plt.clf()
#print(flight.shape)

# 10-minutes delay is fairly common for this airlines. 

## Task 4
perc = 0.1
flight_sub = flight.sample(n = int(flight.shape[0]*perc))

#sns.lmplot(x = "coach_price", y = "firstclass_price", data = flight_sub, line_kws= {'color': 'black'}, lowess=True)
#plt.show()
#plt.clf()

## Task 5

# Inflight meal
#sns.histplot(flight, x = "coach_price", hue = flight.inflight_meal)
#plt.show()
#plt.clf()

#sns.boxplot(x="inflight_meal", y="coach_price", data=flight)

#sns.histplot(flight, x = "coach_price", hue = flight.inflight_entertainment)
#sns.boxplot(x = "inflight_entertainment", y = "coach_price", data = flight)
# Higher coach price median for flight with inflight entertainment compare to flight without entertainment
#plt.show()
#plt.clf()

#sns.histplot(flight, x = "coach_price", hue = flight.inflight_wifi)
#sns.boxplot(x = "inflight_wifi", y = "coach_price", data = flight)
# The median coach price in relatively higher for a flight with inflight wifi
#plt.show()
#plt.clf()

## Task 6
#sns.lmplot(x = "hours", y = "passengers", data = flight, x_jitter = 0.25, scatter_kws = {"s": 5, "alpha":0.2}, fit_reg = False)
#plt.show()
#plt.clf()

## Task 7
#sns.lmplot(x = "coach_price", y = "firstclass_price", data = flight_sub, hue = "weekend", fit_reg = False)
#plt.show()
#plt.clf()

## Task 8
sns.boxplot(x = "day_of_week", y = "coach_price", hue = "redeye", data = flight)
plt.show()
plt.clf()



