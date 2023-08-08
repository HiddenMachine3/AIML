import pandas as pd
import numpy as np
from numpy import matmul
from numpy.linalg import inv

"""
e = (yi−^yi)
y = Xw + e
Err=∑(e_i)^2
predicted value of our target: ^y
residual vector : e
"""

# calculating w,y_pred when X,y are given
x1 = np.array([1, 2, 5])
x2 = np.array([1, 3, 5])
x3 = np.array([1, 4, 7])
X = np.array([x1, x2, x3])

y = np.array([1, 1, 3])  # y is a vector, so whether its a 1 by 3 or 3 by 1 matrix shouldn't matter much

w = matmul(matmul(inv(matmul(X.T, X)), X.T), y)

# x = np.array([1, 5, 8])

print("X:", X, "y:", y, "w:", w, sep="\n")
#
# y_pred = np.inner(x, w)
# print("y^ =", y_pred)


######calculating y when X and w are given
# x1 = np.array([1, 2, -3, 5])
# x2 = np.array([1, 0.2, -3, 4])
# x3 = np.array([1, 1, 0, 6])
# X = np.array([x1, x2, x3])
#
# w = np.array([-1.8, 2, -4, 0.2])
#
# y = matmul(X,w)  # y is a vector, so whether its a 1 by 3 or 3 by 1 matrix shouldn't matter much
#
# print("X:", X, "w:", w,"y:", y,  sep="\n")
# print("y_total:", y.sum())
