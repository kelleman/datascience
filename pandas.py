import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv("data.csv")
print(df)
print(df.describe())
x = df['score']
y = df['coursecode']
g = df['grades']
print(x)
print(y)
print(g)
plt.pie(x,labels=g) 