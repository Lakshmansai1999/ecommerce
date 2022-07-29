import pandas as pd

df = pd.read_csv('tab.csv', nrows=2)
for dtype in df.dtypes.iteritems():
    print(dtype)

for value in df.values.iteritems():
    print(value)
