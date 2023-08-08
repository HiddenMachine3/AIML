import pandas as pd

data = pd.DataFrame([[-2, -1, 0, 1, 2], [2, 1, 0, -1, 2], [1.5, 1, 0, -0.5, 9]])
data = data.T
data.columns = (['X1', 'X2', 'Yi'])
print(data)


def mse(df, y_func):
    res = 0
    for index, row in df.iterrows():
        res += ((row['Yi'] - y_func(row['X1'], row['X2'])) ** 2)
    res /= df.shape[0]
    return res


funcs = [lambda x1, x2: 0.5 + 2 * x1 + 3 * x2,
         lambda x1, x2: -0.5 + 2 * x1 + 3 * x2,
         lambda x1, x2: 2 * x1 + 3 * x2,
         lambda x1, x2: 3 * x1 + 2 * x2]

for func in funcs:
    print(mse(data, func))
