from matplotlib import pyplot as plt
import pandas as pd

df = df = pd.read_csv("companylist.csv")

x = range(100)
y = df['LastSale'].head(100)
for i in y :
    round(i, 1)

plt.plot(x, y)
plt.xlabel('stt')
plt.ylabel('LastSale')
plt.show()