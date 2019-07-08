import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 单一数据
data = pd.Series(np.random.randn(1000),index=np.arange(1000))
data = data.cumsum()
data.plot()
plt.show()

# 多维数据
data = pd.DataFrame(np.random.randn(1000,4),index=np.arange(1000),columns=list("ABCD"))
data = data.cumsum()
data.plot()
plt.show()

# 多维数据-散点图
ax = data.plot.scatter(x='A', y='B', color='DarkBlue', label="Class 1(A/B)")
bx = data.plot.scatter(x='A', y='C', color='LightBlue', label="Class 2(A/C)",ax=ax)
data.plot.scatter(x='A', y='D', color='LightGreen', label='Class 3(A/D)', ax=bx)
plt.show()