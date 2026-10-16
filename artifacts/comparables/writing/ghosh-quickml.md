---
author: "Dibya Ghosh"
org: "UC Berkeley"
url: "https://dibyaghosh.com/blog/ml/quickml/"
date: "n.d."
fetch_date: "2026-10-15"
connects_to: "Dibya Ghosh (OpenAI/Anthropic list)"
why_it_matters: "Example of a researcher publishing reusable tooling and notes as part of a public body of work."
---

# QuickML

A simple and clean presentation of code for nearest neighbors, linear regression, and logistic regression. We've carefully written the code to make it as close to pseudocode as possible.

A quick beginner’s guide to coding the fundamental algorithms in ML has been on my todo-list for a while. Heavily inspired by Napkin ML

### Table of Contents

More coming soon!

This post hides some of the boilerplate code: if you want to extend these tutorials or play around with them, check them out here

### The Basic Imports

A machine learner never leaves home without NumPy

Warning: If you don’t know NumPy, then this article may be difficult to comprehend. The Scipy Lectures are a good resource.

```
```
import numpy as np
```
```

### Introducing our Dataset

We’ll use a simple 2 dimensional nonlinear dataset to run our algorithms, so that it’s easier to visualize, yet complex enough that we see different types of behaviour from different algorithms.

```
```
# See Github for the full code - hidden for brevity
Xs = ...
Ys = ...
test_Xs = ...
test_Ys = ...

def accuracy(model,X,Y):
    pass 
def plot(model,X,Y):
    pass
```
```

For each algorithm, we’ll train it on a dataset with 1000 samples, and plot the decision curve learned by the algorithm. For example, here’s the “optimal” classifier. The color of the point is the true class, and the color of the background is what the classifier predicts.

### Show the code

```
```
import matplotlib.pyplot as plt
%matplotlib inline

Xs = np.random.rand(1000,2)*10
Ys = np.array([x[1] > x[0]+np.sin(x[0]*2) for x in Xs])

test_Xs = np.random.rand(1000,2)*10
test_Ys = np.array([x[1] > x[0]+np.sin(x[0]*2) for x in test_Xs])

def accuracy(model,X,Y):
    return np.count_nonzero([model.predict(x)==y for (x,y) in zip(X,Y)])/len(X)

def plot(model,X,Y,shades=False,nPoints=100,**kwargs):
    plt.figure(figsize=(8,8))
    h = 100
    x_min, y_min = np.min(X,axis=0)
    x_max, y_max = np.max(X,axis=0)
    
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, h),
                         np.linspace(y_min, y_max, h))

    # here "model" is your model's prediction (classification) function
    Z = np.array([model.predict(x) for x in np.c_[xx.ravel(), yy.ravel()]])

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, cmap=plt.cm.Pastel2,**kwargs)
    subpoints = np.random.choice(len(X),nPoints)
    plt.scatter(X[subpoints, 0], X[subpoints, 1], c=Y[subpoints], cmap=plt.cm.Dark2)
    plt.axis('off')

    # Plot also the training points
class Dummy:
    def predict(x):
        return x[1] > x[0]+np.sin(x[0]*2)
plot(Dummy,Xs,Ys)
```
```

## K-Nearest Neighbors

$k$-Nearest Neighbors is a non-parametric machine learning model that predicts classes for points x based on the k closest values to x seen in the training set.

```
```
from collections import Counter

class kNN:
    def __init__(self,k=1):
        self.k = k
  
    def fit(self,xs,ys,k=1):
        """
        Since kNN is nonparametric, we need to keep the training data around during test time.
        k-NN doesn't do any additional preprocessing
        """
        self.xs = xs 
        self.ys = ys
  
    def predict(self,x):
        # Sort training points by distance to the new point
        closest_points = np.argsort(np.linalg.norm(self.xs-x,axis=1))[:self.k]
        # Get labels of these close points
        closest_labels = self.ys[closest_points] 
        # Return the most common label
        return Counter(closest_labels).most_common(1)[0][0]
```
```

### Show the code

```
```
kNN_classifier = kNN(1)
kNN_classifier.fit(Xs,Ys)
plot(kNN_classifier,test_Xs,test_Ys)
print("Accuracy is ",accuracy(kNN_classifier,test_Xs,test_Ys))
```
```

```
```
Accuracy is  0.978
```
```

## Linear Regression

Linear regression attempts to find the best linear model $f(x) =w^Tx$ to fit the data. The training procedure revolves around solving the following equation

$$w^\* = \arg\min\_{w \in \mathbb{R}^d} \sum\_{i=1}^n (w^TX\_i - y\_i)^2 $$

We can write this in matrix form, where $X$ is a $n \times d$ matrix where each row corresponds to a training point.

$$w^\* = \arg\min\_{w \in \mathbb{R}^d} \|Xw-y\|\_2^2$$

Using matrix calculus, we have that $\nabla\_w = X^T(Xw-y)$, so the optimal solution $w^\*$ satisfies

$$(X^TX)w^\* = X^Ty$$

```
```
class LinReg:
    def fit(self,xs,ys):
        """
        Solving (X^TX)w^* = X^Ty
        """
        
        self.w = np.linalg.solve(xs.T.dot(xs),xs.T.dot(ys))
  
    def predict(self,x):
        return self.w.dot(x) > 0.5 # If predict >0.5, then say class 1, else class 0
```
```

### Show the code

```
```
linear_classifier = LinReg()
linear_classifier.fit(Xs,Ys)
print("Accuracy is ",accuracy(linear_classifier,test_Xs,test_Ys))
plot(linear_classifier,test_Xs,test_Ys)
```
```

```
```
Accuracy is  0.856
```
```

## Logistic Regression

Logistic regression is similar to linear regression, but specializes to classification tasks by predicting probabilities $p(y\_i=1~\mid~x\_i)$.

If we naively apply linear regression to predicting probabilities, we’ll be maximizing $p(y=1|x) = w^Tx$. However, since $w^Tx$ can be between $(-\infty, \infty)$, it matches poorly to the desired output $(0,1)$.

[Excerpt truncated at the line cap; see url for the remainder.]
