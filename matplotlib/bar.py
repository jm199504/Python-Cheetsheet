import matplotlib.pyplot as plt
import numpy as np

n = 12
X = np.arange(n)

# uniform: 均匀分布 且左闭右开
Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)

# 绘制条形条，设置表明颜色, 边缘颜色
plt.bar(X, +Y1,facecolor='#9999ff',edgecolor='white')
plt.bar(X, -Y2,facecolor='#ff9999',edgecolor='white')

# 设置文字(数字)且确定位置
for x,y in zip(X,Y1):
    # ha: horizontal alignmant
    plt.text(x,y+0.15,'%.2f'%y,ha='center')
for x,y in zip(X,Y2):
    plt.text(x,-y-0.15,'-%.2f'%y,ha='center')

# 设置字体格式（避免设置中文显示异常）
plt.rcParams['font.sans-serif'] = ['SimHei']
# 避免负号显示为方块
plt.rcParams['axes.unicode_minus']=False
# 设置标题
plt.title("条形图")
plt.xlim(-.5, n)
plt.xticks(())
plt.ylim(-1.25, 1.25)
plt.yticks(())
# 显示图表
plt.show()