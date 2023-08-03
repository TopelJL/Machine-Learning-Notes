# Supervised vs. Unsupervised Machine Learning

## Week 1

### What is machine Learning?

Machine Learning -
    "Field of study that gives computers the ability to learn without being explicitly programmed" - Arthur Samuel (1959)

### Machine Learning Algorithms

Supervised Learning - Used most in real world applications, most rapid advancements.

**In this course we will learn practical advice for applying learning algorithms**

### Supervised Learning

**Maps x --> y**
**Learns from being given right answers**

**Two types:**
Regression
    Predict numbers from infinitely many possible outputs.
Classification
    Predict categories from small number of possible outputs.

#### Regression

Algorithms that learn x (input) --> y (output) mappings. Learns from being given the right answers.

examples

1. 
x = email
y = spam? (0/1)
Application = spam filtering

2. 
x = audio
y = text transcripts
Application = speech recognition

3. 
x = English
y = spanish
Application = Machine Translation

**Most lucrative application is online advertising**

4. 
x = ad, user info
y = click? (0/1)
Application = Online advertising

5. 
x = Image, radar info
y = position of other cars
Application = Self-driving car

6. 
x = image of phone
y = defect? (0/1)
Application = Visual inspection


**Regression: Housing prices prediction**

Regression - Predict a number from infinitely many possible outputs

x = house size in feet^2
y = price in $1000's
Application = housing price prediction

#### Classification

**Classification alogorthms predict categories**
Predicts a small finite limited number of possible outputs

Examples

1. 
Breast Cancer Detection - detects whether a tumor is malignant or benign.

x1 = size
y = diagnosis, Benign(0) or malignant(1)
malignant is deadly
begnign is not

Two outputs means this is classification.

Can also output multiple outputs, malignant 1, malignant 2, etc...

**Multiple inputs**

x1 = age
x2 = tumor size
y = malignant(1) or benign(0)

Algoritm finds a boundary that seperates malignant from benign.

### Unsupervised Learning