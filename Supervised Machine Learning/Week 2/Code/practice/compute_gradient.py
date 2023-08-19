# Jaxon Topel
# Description:

import copy, math
import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(precision=2) # reduced display precision on numpy arrays

def compute_gradient(X, y, w, b):
    m,n = X.shape # ((m)number of examples, (n)numerber of features
    dj_dw = np.zeros((n,))
    dj_db = 0
    
    for i in range(m):
        err = (np.dot(x[i], w) + b) - y[i]
        for j in range(n):
            dj_dw[j] = dj_dw[j] + err * X[i, j]
        dj_db = dj_db + err
    dj_dw = dj_dw / m
    dj_db = dj_db / m
    
    return dj_db, dj_dw

#Compute and display gradient 
tmp_dj_db, tmp_dj_dw = compute_gradient(X_train, Y_train, w_init, b_init)
print(f'dj_db at initial w,b: {tmp_dj_db}')
print(f'dj_dw at initial w,b: \n {tmp_dj_dw}')