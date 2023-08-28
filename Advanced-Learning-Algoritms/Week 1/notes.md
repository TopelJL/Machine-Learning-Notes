# Advanced Learning Algoritms


**4 Topics**
- ## (week 1) Neural Networks.
- ## (week 2) Neural Network Training.
- ## (week 3) Advise for appying machine learning.
- ## (week 4) Decision trees.


## (week 1) Neural Networks
- **(Deep Learning Algorithms)**
- Neural Networks intuition
    - Neurons and the brain
        - **Learn how to make better decisions on how to approach practical Deep Learning Algoritms**
        - Neural Netowrks first impacted speech recognition, images (computer vision), text (natural language processing).
        - ![Alt text](image.png)
    - Demand Prediction
        - ![Alt text](image-1.png)
        - Neuron is like a tiny litte computer
        - ![Alt text](image-2.png)
        - hidden layer
            - Each neuron has access to every feature and value from the previous layer
            - it figures out which features to use automatically by setting the parameters appropriately
        - multiple hidden layers
            - ![Alt text](image-3.png)
            - neural network architecture
                - How many layers do you want
                - how many neurons in each layer
                *learn later tips for choosing*
    - Recognizing images
        - ![Alt text](image-4.png)
        - ![Alt text](image-5.png)
        - ![Alt text](image-6.png)
- Neural network model
    - Neural Network Layer
        - *Learn how to construct a layer of neurons.*
        - ![Alt text](image-7.png)
        - Input of Layer 2 is output of layer 1.
        - Uses logistic regression sigmoid function to get activation function for each neuron.
        - ![Alt text](image-8.png)
        - ![Alt text](image-9.png)
        - Every layer inputs a vector of numbers, applies logistic regression and computes another vector of numbers.
    - More Complex Neural networks
        - Neural Network with 4 layers
            - Layers 1, 2, 3 are hidden layers.
            - Input is layer 0
            - Output is layer 4
            - ![Alt text](image-10.png)
    - Inference: making predictions (forward propagation algorithm)
        - *how to get a neural network to make predictions*
        - handwritten digit recognition
        - Compute a[1] - 25 neurons (units)
            - ![Alt text](image-11.png)
        - Compute a[2] - 15 neurons (units)
            - ![Alt text](image-12.png)
        - Compute a[3]
            - ![Alt text](image-13.png)
- Tensorflow implementation
    - Inference in Code
        - ![Alt text](image-14.png)
        - ![Alt text](image-15.png)
    - Data in Tensorflow
        - *how data is represented*
        - ![Alt text](image-16.png)
        - rows * columns
        - ![Alt text](image-17.png)
        - ![Alt text](image-18.png)
        - *Tensor is a way of showing a matrix*
    - Building a neural network
        - *how to build neural network in tensorflow*
        - ![Alt text](image-19.png)
        - ![Alt text](image-20.png)
        - ![Alt text](image-21.png)
- Neural Network implementation in python
    - Forward prop in a single layer
        - ![Alt text](image-22.png)
    - General implementation of forward propagation
        - ![Alt text](image-23.png)
        # Code
        def dense(a_in, W, b):
            units = W.shape[1] # Gets number of units
            a_out = np.zeros(units) # sets array of zeros for number of units
            for j in range(units):
                w = W[:,j]
                z = np.dot(w, a_in) + b[j]
                a_out[j] = g(z)
            return(a_out)
       
        def my_sequential(x, W1, b1, W2, b2):
            a1 = dense(x, W1, b1)
            a2 = dense(a1, W2, b2)
            return(a2)
- Speculations on artificial general intelligence (AGI)
- Vectorization (optional)
*practice lab Neural Networks - see Coursera code*