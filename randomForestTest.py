from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np

X, y = load_iris(return_X_y=True, as_frame=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=17)

clf = RandomForestClassifier(n_estimators=5, max_features=2, random_state=17, oob_score=True)

clf.fit(X_train, y_train)
pdf = pd.DataFrame(data={"predicted_output": clf.predict(X_test)}, index=X_test.index)

print(pd.concat([X_test, pdf, pd.DataFrame(data=clf.predict_proba(X_test), index=X_test.index,
                                           columns=["setosa_prob", "versicolor_prob", "virginica_prob"])], axis=1))

print("accuracy on test data :", clf.score(X_test, y_test))

nan = np.array([0., 0., 0.])
n = 0
for x in clf.oob_decision_function_:
    if np.array_equal(x, nan):
        n += 1

print(n)  # clf.estimators_)
