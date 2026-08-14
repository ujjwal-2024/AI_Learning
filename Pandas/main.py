import pandas as pd

a = {"ujjwal": 22, "sachin": 23, "rahul": 24}
s = pd.Series(a)
print(s)

df = pd.DataFrame([a])
print(df)