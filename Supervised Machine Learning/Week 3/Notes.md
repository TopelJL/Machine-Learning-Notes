# Classification

**Topics covered in this file**
- Use logistic regression for binary classification
- Implement logistic regression for binary classification
- Address overfitting using regularization, to improve model performance
**See Python files to understand machine learning code**

## Week 3

### Classification with logistic regression

#### Motivations

- ![Alt text](image.png)
- ![Alt text](image-1.png)
- Notes:
    - Binary Classification
        - false = 0
        - True = 1

#### Logistic Regression
- Most used classification algorithm
- Classifying whether a tumor is maligant (1) or benign (0)
- ![Alt text](image-2.png)
- In the logistic regression model, it takes two equations z and uses it in equation g.
- "probability" that class is 1.
#### Decision Boundaries
- ![Alt text](image-4.png)
-![Alt text](image-3.png)
### Cost function for logistic regression
- ![Alt text](image-5.png)
- Squared error is not a good choice for logistic regression
- ![Alt text](image-6.png)
- When y = 1
    - ![Alt text](image-7.png)
- When y = 0
    - ![Alt text](image-8.png)
- **New Definition for loss function for logistic regression.**
- ![Alt text](image-9.png)
#### Simplified Loss/Cost function
- Use this function for gradient descent
- ![Alt text](image-11.png)
#### Gradient Descent implementation
- ![Alt text](image-12.png)
- ![Alt text](image-13.png)
### Overfitting