# Jaxon Topel
# Description: 
    # Utilize multiple variable routines developed in the previous lab
    # Run Gradient Descent on a dataset with multiple features
    # explore the impact of the learning rate alpha on gradient descent
    # improve performance of gradient descent by feature scaling using z-score normalization. (See week 2 notes for z-score formula)
    
import numpy as np
import matplotlib.pyplot as plt
from lab_utils_multi import load_house_data, run_gradient_descent
from lab_utils_multi import norm_plot, plt_equal_scale, plot_cost_i_w
from lab_utils_common import dlc
np.set_printoptions(precision=2)


# Load the dataset
X_train, y_train = load_house_data()
X_features = ['size(sqft)', 'bedrooms', 'floors', 'age']

fig,ax = plt.subplots(1, 4, figsize = (12,3), sharey = True)
for i in range(len(ax)):
    ax[i].scatter(X_train[:i],y_train)
    ax[i].set_xlabel(X_features[i])
ax[0].set_ylabel("Price (1000's)")
plt.show

