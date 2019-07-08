import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 设置画布
fig = plt.figure()
# 设置3D坐标轴
ax = Axes3D(fig)
# 创建数据集
X = np.arange(-4,4,0.25)
Y = np.arange(-4,4,0.25)
X,Y = np.meshgrid(X,Y)
R = X+Y
Z = np.sin(R)

# 绘制3D图
# rstride/cstride:表示步伐大小，其越小超平面过渡越细致
ax.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap=plt.get_cmap('rainbow'))

# 设置是否将Z轴投影到XY平面
# offset表示底部2D平面的y轴坐标面
# ax.contourf(X,Y,Z,zdir='z',offset=-2,cmap='rainbow')

ax.set_zlim(-2,2)

plt.show()