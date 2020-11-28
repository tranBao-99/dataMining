import pandas as pd
import numpy as np

# standard missing values

df = pd.read_csv("companylist.csv")

# print(df['Symbol'])
# print(df["Symbol"].isnull())

missing_values = ["n/a", "na", "--"]
df = pd.read_csv("companylist.csv", na_values = missing_values)

# print(df.isnull().any())

df = df.dropna(axis = 'index',how = 'all', subset=['MarketCap', 'Sector', 'industry'])

df = df.sort_values(by = 'MarketCap', ascending=False)


print(df)

