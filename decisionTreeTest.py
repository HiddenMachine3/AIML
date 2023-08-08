import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

link = "http://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data"
df = pd.read_csv(link, header=None)
df.dropna(inplace=True, how="any", axis=0)
df[60].replace(['M', 'R'], [0, 1], inplace=True)

X = df.drop(60, axis=1)
y = df[60]

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=34)

# clf = DecisionTreeClassifier(criterion="gini", random_state=34)
# clf.fit(x_train, y_train)
# print("\ncriterion=gini, accuracy on test data:", clf.score(x_test, y_test))

clf = DecisionTreeClassifier(criterion="entropy", random_state=34, max_depth=4, max_features=1, min_samples_split=5)
clf.fit(x_train, y_train)
print("\ncriterion=entropy, accuracy on test data:", clf.score(x_test, y_test))

print("Decision tree depth :", clf.get_depth())
