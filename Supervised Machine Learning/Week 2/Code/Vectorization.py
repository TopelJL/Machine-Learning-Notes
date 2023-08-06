# Jaxon Topel
# Description: Use Numpy and Python to compute vectorization

import numpy as np
import time

# NumPy routines which allocate memory and fill arrays with value
a = np.zeros(4)
print(f"np.zeros(4): a = {a}, a shape = {a.shape}, a datatype = {a.dtype}")
a = np.zeros((4,))
print(f"np.zeros(4): a = {a}, a shape = {a.shape}, a datatype = {a.dtype}")
np.random.random_sample(4)
print(f"np.random.random_sample(4): a = {a}, a shape = {a.shape}, a datatype = {a.dtype}")

# NumPy routines which allocate memory and fill arrays with value but do not accept shape as input argument
a = np.arange(4,)
print(f"np.array([5,4,3,2]): a = {a}, a shape = {a.shape}, a data type = {a.dtype}")
a = np.random.rand(4)
print(f"np.random.rand(4): a = {a}, a shape = {a.shape}, a data type = {a.dtype}")

# NumPy routines which allocate memory and fill with user specified values
a = np.array([5,4,3,2])
print(f"np.array([5,4,3,2]): a = {a}, a shape = {a.shape}, a datatype = {a.dtype}")
a = np.array([5.,4,3,2])
print(f"np.array([5,4,3,2]): a = {a}, a shape = {a.shape}, a datatype = {a.dtype}")

# Indexing means referring to an element of an array by its position within the array
# Slicing means getting a subset of elements from an array based on their indices.

# Vector indexing operations on 1-D vectors.
a = np.arange(10)
print(a)

# access an element
print(f"a[2].shape = {a[2].shape}, a[2] = {a[2]}, accessing an element returns a scalar")

# access the last element, negative indezes count from the end
print(f"a[-1] = {a[-1]}")

# indexes must be within the range of the vector or they will produce an error
try:
    c = a[10]
except Exception as e:
    print(f"you caught an error little buddy: {e}")
    
# Vector Slicing operations
a = np.arange(10)
print(f"a = {a}")

# Access 5 consecutive elements (start:stop:step)
c = a[2:7:1]
print(f"a[2:7:1] = {c}")
# Access 3 elements seperated by two
c = a[2:7:2]
print(f"a[2:7:2] = {c}")
# Access all elements above index 3
c = a[3:]
print(f"a[3:] = {c}")
# Access all elements below index 3
c = a[:3]
print(f"a[:3] = {c}")
# Access all elements
c = a[:]
print(f"a[:] = {c}")

# Single vector operations
a = np.array([1,2,3,4])
print(f"a = {a}")

# Negate elements of a
b = -a
print(f"b = -a --> {b}")
# Sum all elements of a, returns a scalar
b = np.sum(a)
print(f"sum of array = {b}")
# mean
b = np.mean(a)
print(f"Mean = {b}")
# Square the array
b = a**2
print(f"a^2 = {b}")

# Vector Vector element-wise operations
a = np.array([1,2,3,4])
b = np.array([-1,-2,3,4])
print(f"Binary operators work element wise: {a+b}")

# Scalar Vector Operations
a = np.array([1,2,3,4])
# multiply by a scalar
b = 5*a
print(f"5 * a = {b}")

# Vector Vector Dot Product using for loop (assume a and b are same shape)
def my_dot(a ,b):
    x = 0
    for i in range(a.shape[0]):
        x = x + a[i] * b[i]
    return x

# Test 1-D
a = np.array([1,2,3,4])
b = np.array([-1,4,3,2])
print(f"my_dot(a,b) = {my_dot(a, b)}")

# Now use np.dot()

# Test 1-D
a = np.array([1,2,3,4])
b = np.array([-1,4,3,2])
c = np.dot(a,b)
print(f"NumPy 1-D np.dot(a,b) = {c}, np.dot(a, b).shape = {c.shape}")
c = np.dot(b,a)
print(f"NumPy 1-D np.dot(b,a) = {c}, np.dot(b, a).shape = {c.shape}")

# Lets improve that code
np.random.seed(1)
a = np.random.rand(10000000) # Very Large array
b = np.random.rand(10000000) # Very Large array

tic = time.time() # Capture start time
c = np.dot(a, b)
toc = time.time() # Capture end time

print(f"np.dot(a, b) = {c:0.4f}")
print(f"Vectorized version duration: {1000*(toc-tic):0.4f} ms")

# The Below comments are deleted as it takes a long time to perform this operation and need speedy code in practice :)

#tic = time.time() # Capture start time
#c = my_dot(a, b)
#toc = time.time() # Capture end time
#print(f"my_dot(a, b) = {c:0.4f}")
#print(f"loop version duration: {1000*(toc-tic):0.4f} ms")

# Now remove these big arrays
del(a)
del(b)

# Matrices are denoted with capital letters
# m =  number of rows
# n =  number of columns
a = np.zeros((1,5))
print(f"a shape = {a.shape}, a = {a}")

a = np.zeros((2,1))
print(f"a shape = {a.shape}, a = {a}")

a = np.random.random_sample((1,1))
print(f"a shape = {a.shape}, a = {a}")

# NumPy routines which allocate memory and fill with user specified values
a = np.array([[5], [4], [3]])
print(f"a shape = {a.shape}, np.array: a = {a}")

# Vector indexing operations on matrices (m, n), where m is rows and columns is n
a = np.arange(6).reshape(3,2) # Reshape is a convenient way to create matrices
print(f"a.shape = {a.shape}, a = {a}")

# access an element
print(f"a[2,0].shape = {a[2,0].shape}, a[2,0] = {a[2,0]}, type(a[2,0]) = {type([2,0])}") # Accessing an element returns a scalar

# access a row
print(f"a[2].shape = {a[2].shape}, a[2] = {a[2]}, type(a[2]) = {type(a[2])}")

#vector 2-D slicing operations
a = np.arange(20).reshape(-1, 10)
print(f"a = \n{a}")

#access 5 consecutive elements (start:stop:step)
print("a[0, 2:7:1] = ", a[0, 2:7:1], ",  a[0, 2:7:1].shape =", a[0, 2:7:1].shape, "a 1-D array")

#access 5 consecutive elements (start:stop:step) in two rows
print("a[:, 2:7:1] = \n", a[:, 2:7:1], ",  a[:, 2:7:1].shape =", a[:, 2:7:1].shape, "a 2-D array")

# access all elements
print("a[:,:] = \n", a[:,:], ",  a[:,:].shape =", a[:,:].shape)

# access all elements in one row (very common usage)
print("a[1,:] = ", a[1,:], ",  a[1,:].shape =", a[1,:].shape, "a 1-D array")
# same as
print("a[1]   = ", a[1],   ",  a[1].shape   =", a[1].shape, "a 1-D array")
