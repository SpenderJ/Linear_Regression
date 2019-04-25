#!/usr/bin/python3
from numpy import *
import pandas as pd
import matplotlib.pyplot as plt

# Important thing, this function is concepted to be global

# import our file
input_file = "data.csv"
output_file = "teta.txt"

# load our file to dataset
try:
    dataset = pd.read_csv(input_file, delimiter=",", dtype="float")
except Exception as e:
    exit(e)
# Spliting our dataset into 2 separated columns | We begin at 1 so we don't have column name
X = dataset.iloc[0:len(dataset), 0]
Y = dataset.iloc[0:len(dataset), 1]

# Born Definition

mixY = min(Y)
maxY = max(Y)
minX = min(X)
maxX = max(X)

x = (X - minX) / (maxX - minX)
y = (Y - mixY) / (maxY - mixY)

# Visu

axes = plt.axes()
axes.grid() # draw grid

# End visu for now

# Set our variables

m = len(X)  # M is the number of experience our dataset contain
alpha_rate = 0.1  # Learning rate - Change value to change algo
initial_t0 = 0  # use for tmp t0 final value will be used
initial_t1 = 0  # use for tmp t1 final value will be used
iteration = 1000  # number of it

# Create true func


def launch_gradient_descent():
    tmp_t0 = 0
    tmp_t1 = 0
    for every in range(0, iteration):
        sum1 = 0
        sum2 = 0
        for i in range(0, m):
            sum1 += ((tmp_t1 * x[i] + tmp_t0) - y[i])
            sum2 += (((tmp_t1 * x[i] + tmp_t0) - y[i]) * x[i])
        tmp_t0 = tmp_t0 - (alpha_rate * (sum1 / m))
        tmp_t1 = tmp_t1 - (alpha_rate * (sum2 / m))
    return [tmp_t0, tmp_t1]


[final_t0, final_t1] = launch_gradient_descent()


# End func

# Added for line

def normalize(lstX, x):
    return (x - min(lstX)) / (max(lstX) - min(lstX))


def denormalize(lstX, x):
    return x * (max(lstX) - min(lstX)) + min(lstX)


# End

# Visu print

lx = [minX, maxX]
ly = []
for j in lx:
    j = final_t1 * normalize(X, j) + final_t0
    price = denormalize(Y, j)
    ly.append(price)

plt.scatter(X, Y)
plt.plot(lx, ly, color='red')
plt.show()

# End of visu

# Output in the file

with open(output_file, 'w') as f:
    f.write(str(final_t0))
    f.write("\n")
    f.write(str(final_t1))
