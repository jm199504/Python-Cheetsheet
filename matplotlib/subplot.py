import matplotlib.pyplot as plt

# 设置画布，默认第一块画布
plt.figure()

# 在2×2中选取第一块区域
plt.subplot(2,2,1)
# 绘制点线图[0,0]到[1,1]
plt.plot([0,1],[0,1])

# 在2×2中选选取第二块区域
plt.subplot(2,2,2)
# 绘制点线图[0,0]到[1,2]
plt.plot([0,1],[0,2])

plt.subplot(2,2,3)
plt.plot([0,1],[0,3])

plt.subplot(2,2,4)
plt.plot([0,1],[0,4])

# 设置第二块画布
plt.figure(num=2)

plt.subplot(2,1,1)
plt.plot([0,1],[1,1])

plt.subplot(2,3,4)
plt.plot([0,1],[0,2])

plt.subplot(2,3,5)
plt.plot([0,1],[0,2])

plt.subplot(2,3,6)
plt.plot([0,1],[0,2])

plt.show()