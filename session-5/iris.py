import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

# Load data from sklearn
X, y = load_iris(return_X_y=True)

# Train the model using regresion logistic
clf = LogisticRegression(solver='lbfgs',
                         max_iter=1000,
                         multi_class='multinomial').fit(X, y)
# Define iris types
<< << << < HEAD
iris_type = {0: 'setosa', 1: 'versicolor', 2: 'virginica'
             }
== == == =
iris_type = {
    0: 'setosa',
    1: 'versicolor',
    2: 'virginica'
}
>>>>>> > d2ec574135b3f53215db217593e5b435cd9e85b1


# Define dummy values
sepal_length, sepal_width, petal_length, petal_width = 2, 3, 4, 6

<< << << < HEAD

== == == =
>>>>>> > d2ec574135b3f53215db217593e5b435cd9e85b1
X = [sepal_length, sepal_width, petal_length, petal_width]


# Make a prediction

prediction = clf.predict_proba([X])
print({'class': iris_type[np.argmax(prediction)],
      'probability': round(max(prediction[0]), 2)})
