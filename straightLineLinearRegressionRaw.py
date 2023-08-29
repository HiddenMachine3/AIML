import pandas as pd

data = pd.DataFrame([[1, 2, 3, 4, 5], [5.3, 6.3, 4.8, 3.8, 3.3]])
data = data.T
data.columns = (['x', 'y'])
print(data)

n = data.shape[0]

# df = pd.DataFrame(data=[data.x, data.y, data.x * data.y]).T
# df.columns = ['x', 'y', 'x*y']
# print(df)

a = (n * sum(data.x * data.y) - data.x.sum() * data.y.sum()) \
    / (n * sum([x ** 2 for x in data.x]) - (data.x.sum() ** 2))

b = (data.y.sum() - a * data.x.sum()) / n

print("a:", a, "b:", b)
print(f"y = {a}x + {b}")