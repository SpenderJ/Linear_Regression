#!/usr/bin/python3
import pandas as pd

# Important thing, this function is concepted to be global

input_data_file = "data.csv"
input_teta_file = "teta.txt"

str_to_get = "Please enter a mileage :\n"

try:
    data = pd.read_csv(input_data_file, dtype = "float")
except Exception as e:
    exit(e)
t0 = 0
t1 = 0

X = data.iloc[0:len(data), 0]
Y = data.iloc[0:len(data), 1]

try:
    f = open(input_teta_file)
    t0 = float(f.readline())
    t1 = float(f.readline())
except Exception as e:
    t0 = 0

studied_value = input(str_to_get)
try:
    studied_value = float(studied_value)
    studied_value = (studied_value - min(X)) / (max(X) - min(X))
except Exception as e:
    exit(e)

print("Estimate price :")
result = t1 * studied_value + t0
if result > 0:
    result = result * (max(Y) - min(Y)) + min(Y)
print(result)
