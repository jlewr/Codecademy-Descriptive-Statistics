import pandas as pd
import numpy as np

car_eval = pd.read_csv('car_eval_dataset.csv')
print(car_eval.head())

# What columns do we have?
# ['buying_cost', 'maintenance_cost', 'doors', 'capacity', 'luggage', 'safety', 'acceptability', 'manufacturer_country']

# Table of frequencies
country_freq = car_eval['manufacturer_country'].value_counts()

# EX1 Top and 4th top frequent countries
print("The modal category (most frequent country) is " + str(country_freq.index[0]))
print("The 4th most frequent country is " + str(country_freq.index[3]) + ".")

# EX2 Table of proportions for manufacturer country
country_prop = car_eval['manufacturer_country'].value_counts(normalize = True)

print(country_prop)
# 22.8% of the cars were manufactured in Japan

# EX3 Print possible values for buying_cost
print(car_eval['buying_cost'].unique())

# EX4 Order buying_cost from low to high
buying_cost_categories = ['low', 'med', 'high', 'vhigh']

# EX5 Convert list into category type
car_eval['buying_cost'] = pd.Categorical(car_eval['buying_cost'], buying_cost_categories, ordered = True)

# EX6 Calculate median
median_cat_int = np.median(car_eval['buying_cost'].cat.codes)
median_cat = buying_cost_categories[int(median_cat_int)]

print("The median category is " + str(median_cat))

# EX7 Table of proportions for luggage
luggage_prop = car_eval['luggage'].value_counts(normalize = True)
print(luggage_prop)

# EX8 Check for missing values
luggage_prop_all = car_eval['luggage'].value_counts(dropna = False, normalize = True)
print(luggage_prop_all)

# EX9 Proportions without normalising value_counts()
without_norm = (car_eval['luggage'].value_counts())/len(car_eval['luggage'])

# EX10 Count number of cars with 5+ doors

fiveplusdoors = (car_eval['doors'] == '5more').sum()
print('The number of cars in the dataset with more than five doors is ' + str(fiveplusdoors))

# EX11 Proportion of cars with 5+ doors

fiveplusdoors_pc = (car_eval['doors'] == '5more').mean()
print('The proportion of cars in the dataset with more than five doors is ' + str(fiveplusdoors_pc * 100))

