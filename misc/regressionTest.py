from sklearn.dummy import DummyRegressor

import numpy as np
from sklearn.dummy import DummyRegressor
from sklearn.linear_model import LinearRegression

X = np.array([[1.0], [2.0], [3.0], [4.0]])
y = np.array([2.0, 3.0, 5.0, 10.0])
dummy_regr = LinearRegression()
dummy_regr.fit(X, y)
print(dummy_regr.predict(X))
dummy_regr.score(X, y)
