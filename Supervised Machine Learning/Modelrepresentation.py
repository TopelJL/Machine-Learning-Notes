# Jaxon Topel
# Description: Implement linear regression model with one variable

import numpy as np
import matplotlib.pyplot as plt

# x_train is the input variable (size in 1000 square feet)
# y_train is the target variable (price in 1000's of dollars)
x_train = np.array([1.2, 2.0])
y_train = np.array([300.0, 500.0])
print(f"x_train = {x_train}")
print(f"y_train = {y_train}")

# m is the number of training examples
print(f"x_train.shape: {x_train.shape}")
m = x_train.shape[0]
print(f"Number of training examples is {m}")

i = 0 # Change this to 1 to see (x^1, y^1)

x_i = x_train[i]
y_i = y_train[i]
print(f"(x^({i}), y^({i})) = ({x_i}, {y_i})")

# plot the data points
plt.scatter(x_train,y_train, marker = 'x', c = 'r')
# Set the title
plt.title("Housing prices")
# Set the y-axis label
plt.ylabel('price(in 1000s of dollars)')
# set the x-axis label
plt.xlabel('Size (1000 sqft)')
# Show the plot
plt.show

w = 200 # parameter: weight
b = 100 # parameter: bias

print(f"weight: {w}")
print(f"bias: {b}")

def compute_model_output(x, w, b):
    m = x.shape[0]
    f_wb = np.zeros(m)
    for i in range(m):
        f_wb[i] = w * x[i] + b
    
    return f_wb

tmp_f_wb = compute_model_output(x_train, w, b)

# Plot our model prediction
plt.plot(x_train, tmp_f_wb, c = 'b', label = 'Our Prediction')

# Plot the data points
plt.scatter(x_train, y_train, marker = 'x', c = 'r', label = 'Actual Values')

# Set the title
plt.title("Housing prices")

# set the y-axis
plt.ylabel = ('price(in 1000s of dollars)')

# Set the x-axis
plt.xlabel('Size (1000 sqft)')

plt.legend()
plt.show()