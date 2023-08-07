# Regression with multiple input variables
- **See Python files to understand machine learning code**
- **Topics covered in this file**
- Multiple Linear Regression.
- Gradient Descent in practice.
## Multiple Linear Regression
*See Vectorization.py for code*
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
*How Vectorization works*
- ![Alt text](image-5.png)
- Computer gets all values of vectors w and x, and in a single step multiplies each pair in parallel.
- Takes the numbers to add them all together efficiently.
- Can perform code with vectorization much faster, very beneficial to large models.

**Example**
- Vectors W and d.
- W = W - (0.1) * d
- ![Alt text](image-6.png)

#### Gradient desent for multiple linear regression
*See GradientVec.py for code*
- Review so far.
- ![Alt text](image-7.png)
- Gradient descent with multiple features.
- ![Alt text](image-8.png)
- Alternative to gradient descent, works only with linear regression.
    - Solve for w and b without iterations
    - ![Alt text](image-9.png)