import pandas as pd
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

max_depths = [i for i in range(1, 8)]
depths = []
train_scores = []
test_scores = []

for m_depth in max_depths:
    X, y = load_iris(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
    clf = DecisionTreeClassifier(random_state=42, max_depth=m_depth)
    clf.fit(X_train, y_train)
    train_scores.append(clf.score(X_train, y_train))
    test_scores.append(clf.score(X_test, y_test))
    depths.append(clf.get_depth())

print(pd.DataFrame({"max_depth": max_depths, "train_score": train_scores, "test_score": train_scores,
                    "depth": depths}))  # , columns=[, , , index="max_depth"))
