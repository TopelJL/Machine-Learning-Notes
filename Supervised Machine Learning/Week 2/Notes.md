# Regression with multiple input variables
**Topics covered in this file**
- Multiple Linear Regression.
- Gradient Descent in practice.
**See Python files to understand machine learning code**

## Multiple Linear Regression
- Linear Regression with multiple features
#### Multiple features
- x_j = jth feature.
- n = number of features.
- x(i) = features of ith training example.
- x_j(i) = value of feature j in ith training example.
- ![Alt text](image.png)
- ![Alt text](image-1.png)
- ![Alt text](image-2.png)
- w and b are both parameters, 'w' is a vector & 'b' is a number.
- Use the dot product between vector 'w' and vector 'x'.

#### Vectorization Part 1
*Makes code shorter and more efficiently*
- Parameters and feautres
    - Numerical Linear Algebra Library: *NumPy*
    - ![Alt text](image-3.png)
    - Best practice code:
        - **f = np.dot(w,x) + b**
        - one line of code, and is much faster
    - ![Alt text](image-4.png)
#### Vectorization Part 2
