# Q1. You are given a dataset that contains daily COVID-19 cases for five countries over a 7-day period. Each row represents a day, and each column represents a country. The data is as follows:
# covid_data = np.array([ [1500, 2000, 1800, 1200, 900], # Day 1 
# [1600, 2100, 1900, 1300, 950], 	# Day 2 
# [1700, 2200, 2000, 1400, 1000], 	# Day 3 
# [1650, 2150, 1950, 1350, 980], 	# Day 4 
# [1750, 2250, 2050, 1450, 1020], 	# Day 5 
# [1800, 2300, 2100, 1500, 1050], 	# Day 6 
# [1900, 2400, 2200, 1600, 1100], 	# Day 7 
# ])
# Each column corresponds to:
# Country 1: Country_A
# Country 2: Country_B
# Country 3: Country_C
# Country 4: Country_D
# Country 5: Country_E
# Perform following tasks:
# Basic Statistics:
# Calculate the total number of cases reported in each country over the 7 days.
# Determine the country with the highest total cases.
# Daily Analysis:
# Calculate the average number of cases reported per day across all countries.
# Identify the day with the highest total number of cases across all countries.
# Trends:
# Calculate the percentage increase or decrease in cases for each country from Day 1 to Day 7.
# Find the country with the highest percentage increase.
# Data Transformation:
# Normalize the data (scale all values between 0 and 1) for each country to compare trends more effectively.
# Provide the normalized dataset.
# Visualize the data:
# A line chart showing daily cases for each country
# Highlight the day with the highest total cases across all countries using an annotation or marker.


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Dataset
covid_data = np.array([
    [1500, 2000, 1800, 1200, 900],  # Day 1
    [1600, 2100, 1900, 1300, 950],  # Day 2
    [1700, 2200, 2000, 1400, 1000], # Day 3
    [1650, 2150, 1950, 1350, 980],  # Day 4
    [1750, 2250, 2050, 1450, 1020], # Day 5
    [1800, 2300, 2100, 1500, 1050], # Day 6
    [1900, 2400, 2200, 1600, 1100], # Day 7
])

countries = ['Country_A', 'Country_B', 'Country_C', 'Country_D', 'Country_E']

# Basic Statistics
total_cases_per_country = np.sum(covid_data, axis=0)
country_with_highest_cases = countries[np.argmax(total_cases_per_country)]

# Daily Analysis
average_cases_per_day = np.mean(covid_data)
day_with_highest_cases = np.argmax(np.sum(covid_data, axis=1)) + 1

# Trends
percentage_change = ((covid_data[-1] - covid_data[0]) / covid_data[0]) * 100
country_with_highest_percentage_increase = countries[np.argmax(percentage_change)]

# Data Transformation (Normalization)
normalized_data = (covid_data - np.min(covid_data, axis=0)) / (np.max(covid_data, axis=0) - np.min(covid_data, axis=0))

# Output Results
print("Total cases per country over 7 days:", total_cases_per_country)
print("Country with highest total cases:", country_with_highest_cases)
print("Average cases per day across all countries:", average_cases_per_day)
print("Day with the highest total cases:", day_with_highest_cases)
print("Percentage change in cases from Day 1 to Day 7 for each country:", percentage_change)
print("Country with highest percentage increase:", country_with_highest_percentage_increase)
print("Normalized dataset:\n", pd.DataFrame(normalized_data, columns=countries))

# Visualization
plt.figure(figsize=(10, 6))

# Line chart
for i, country in enumerate(countries):
    plt.plot(range(1, 8), covid_data[:, i], label=country)

# Highlight the day with the highest total cases
total_cases_per_day = np.sum(covid_data, axis=1)
max_day = np.argmax(total_cases_per_day) + 1
plt.axvline(x=max_day, color='red', linestyle='--', label=f'Highest cases (Day {max_day})')

# Formatting
plt.title('Daily COVID-19 Cases per Country')
plt.xlabel('Day')
plt.ylabel('Number of Cases')
plt.xticks(range(1, 8))
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()
