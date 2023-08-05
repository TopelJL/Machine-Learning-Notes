# THIS CODE DOES NOT RUN IN PYTHON, use in jupyter notebook

# Jaxon Topel
# Description: Automate the process of optimizing w and b using gradient descent

import math, copy
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('./deeplearning.mplstyle')
from lab_utils_uni import plt_house_x, plt_contour_wgrad, plt_divergence, plt_gradients

# Load our dataset
x_train = np.array([1.0, 2.0]) # features
y_train = np.array([300.0, 500.0]) # Target Value

# function to calculate the cost
def compute_cost(x, y, w, b):
    m = x.shape[0]
    cost = 0
    
    for i in range(m):
        f_wb = w * x[i] + b
        cost = cost + (f_wb - y[i]) ** 2
    total_cost = 1 / (2 * m) * cost
    
    return total_cost

# by computing the gradient we implement the partial derivatives of the cost function with respect to b and w
def compute_gradient(x,y,w,b):
    m = x.shape[0]
    dj_dw = 0 # derivative with respect to w
    dj_db = 0 # derivative with respect to b
    
    # Loop through training examples
    # mathematical representations of these equations can be found in notes!
    # here we simulatenously update our w and b variables while running through the loop to ensure our steps our in the correct direction
    for i in range(m):
        f_wb = w * x[i] + b
        dj_dw_i = (f_wb - y[i]) * x[i]
        dj_db_i = f_wb - y[i]
        dj_db += dj_db_i
        dj_dw += dj_dw_i
    dj_dw = dj_dw / m
    dj_db = dj_db / m
    
    return dj_dw, dj_db

plt.gradients(x_train, y_train, compute_cost, compute_gradient)
plt.show()

# Performs gradient descent to fit (w, b). Updates (w, b) by taking num_iters gradient steps with learning rate alpha.
def gradient_descent(x, y, w_in, b_in, alpha, num_iters, cost_function, gradient_function):
    # an array to store cost J and w's at each iteration primarilt for graphing later
    J_history = []
    p_history = []
    b = b_in
    w = w_in
    
    for i in range(num_iters):
        # Calculate the gradient and update the paramets using gradient_function
        dj_dw, dj_db = gradient_function(x, y, w, b)
        
        # Update equation using Linear regression gradient descent algorithm
        b = b - alpha * dj_db
        w = w - alpha * dj_dw
        
        # Save cost J at each iteration
        if i < 100000: # Prevent resource exhaustion
            J_history.append(cost_function(x, y, w, b))
            p_history.append([w, b])
            
        # Print cost every at intervals 10 times or as many iteratons if < 10
        if i % math.ceil(num_iters/10) == 0:
            print(f"iteration {i:4}: Cost {J_history[-1]:0.2e} ",
                  f"dj_dw: {dj_dw: 0.3e}, dj_db: {dj_db: 0.3e} ",
                  f"w: {w: 0.3e}, b: {b: 0.5e}")
            
        return w, b, J_history, p_history
    
# Initialize parameters
w_init = 0
b_init = 0

# Gradient Descent Settings
iterations = 10000
tmp_alpha = 1.0e-2

#run gradient descent
w_final, b_final, J_hist, p_hist = gradient_descent(x_train, y_train, w_init, b_init, tmp_alpha, iterations, compute_cost, compute_gradient)

print(f"(w, b) found by gradient descent: ({w_fina;: 8.4f}, {b_final: 8.4f})")

# Plot cost versus iteration
fig, (ax1, ax2) = plt.subplots(1, 2l constrained_layout = True, figsize = (12, 4))
ax1.plot(J_hist[:100])
ax2.plot(1000 + np.arrange(len(J_hist[1000:])), J_hist[1000:])
ax1.set_title("Cost vs. iteration(start)")
ax2.set_title("Cost vs. iteration(end)")
ax1.set_ylabel('Cost')
ax2.set_ylabel('Cost')
ax1.set_xlabel('Iteration Step')
ax2.set_xlabel('Iteration Step')
plt.show()


# Predictions
print(f"1000 sqft house prediction {w_final*1.0 + b_final: 0.1f} Thousand dollars")
print(f"1200 sqft house prediction {w_final*1.2 + b_final: 0.1f} Thousand dollars")
print(f"2000 sqft house prediction {w_final*2.0 + b_final: 0.1f} Thousand dollars")

# Plotting
fig, ax = plt.subplots(1, , figsize - (12, 6))
plt_contour_wgrad(x_train, y_train, p_hist, ax)

# Zooming in
fig, ax = plt.subplots(1, , figsize - (12, 4))
plt_contour_wgrad(x_train, y_train, p_hist, ax, w_range = [180, 220, 0.5], b_range = [80,120,0.5], contours = [1,5,10,20], resolution = 0.5)