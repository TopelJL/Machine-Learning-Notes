# THIS CODE DOES NOT RUN IN PYTHON, Only Jupyter Notebook as it is limited by line #7

# Jaxon Topel
# Description: Use the cost function to predict housing prices given the size of the house.

import numpy as np # Popular library for scientific computing
# %matplotlib Widget --> Jupyter notebook specific
import matplotlib.pyplot as plt # Popular library for plotting data
from lab_utils_uni import plt_intuition, plt_stationary, plt_update_onclick
plt.style.use('./deeplearning.mplstyle')

x_train = np.array([1.0, 2.0]) # Size in 1000 square feet
y_train = np.array([300.0, 500.0]) # price in 1000's of dollars

# f_wb, a prediction is calculated
# the difference between the target and the prediction is calculated and squared
# this is added to the total cost
def compute_cost(x, y, w, b):
    # Compute the cost function for linear regression
    m = x.shape[0]
    # Loop through number of training examples and add each example to 'cost_sum'
    for i in range(m):
        f_wb = w * x[i] + b
        cost = (f_wb - y[i]) ** 2
        cost_sum = cost_sum + cost
    total_cost = (1 / (2*m)) * cost_sum
    
    return total_cost

# Plot 
plt_intuition(x_train,y_train)

# Larger Dataset
plt.close('all')
fig, ax, dyn_items = plt_stationary(x_train,y_train)
updater = plt_update_onclick(fig, ax, x_train, y_train, dyn_items)