from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

# 创建数据集
x = np.random.normal(0, 1, 100)
y = np.random.normal(0, 1, 100)
z = np.random.normal(0, 1, 100)

# 设置画布
fig = plt.figure()
# 建立三维坐标轴
ax = Axes3D(fig)
# 绘制散点图
ax.scatter(x, y, z)
# 显示图表
plt.show()