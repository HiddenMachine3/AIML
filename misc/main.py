import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

X = [[55], [60], [61], [70], [80], [90], [95], [100], [101]]
y = [[0], [1], [1], [1], [1], [1], [1], [1], [0]]
classifier = DecisionTreeClassifier(criterion='entropy', random_state=0)
classifier.fit(X, y)

while(True):
    test_heartbeat = input("Enter a test heartbeat : ");
    X_marks = [[test_heartbeat]]

    prediction = classifier.predict(X_marks);

    text = 'healthy'

    if prediction == 0:
        text='not healthy'

    print(f"test hearbeat/min : {test_heartbeat}, predicted value : {text}")