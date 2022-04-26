import pandas as pd

df = pd.read_csv('../input/sample-dataset/in.csv', header=None)
ds = df.sum(axis=1)

ds.to_csv('out.csv', index=False)
