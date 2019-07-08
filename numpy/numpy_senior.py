import numpy as np

# 创建一个 5x5 的二维数组，其中边界值为1，其余值为0（利用分片法）
A = np.ones((5,5))
A[1:-1,1:-1] = 0
print(A)

# 1、以数字 0 为边界值的全为 1 的 5x5 二维数组（因为并不是邻接区域，分片法要多次）
# np.pad(待填充数组，pad_width=填充的长度，mode=填充的方法，constant_value=填充值)：专门用于对一维数组的填充的方法
# 注意这个方法是对原数组的一个扩展方法
A = np.ones((3,3))
A = np.pad(A, pad_width=1, mode='constant', constant_values=0)
print(A)

# 2、创建一个 5x5 的二维数组，并设置值 1, 2, 3, 4 落在其对角线下方
# numpy.diag(对角线元素=()，k=加入零值行数[注意负号])返回一个矩阵的对角线元素
# 先来个简单demo
A = np.diag((1,2,3),-2)
print(A)
# 加工实现5×5的任务
A = np.diag(1+np.arange(4),k=-1)
print(A)

# 创建一个 10x10 的二维数组，并使得 1 和 0 沿对角线间隔放置（非常简单，用分片法）
A = np.zeros((10,10),dtype=int)
A[1::2,::2] = 1#偶数行
A[::2,1::2] = 1#奇数行
print(A)

# 找出两个一维数组中相同的元素
# np.intersect1d = 求交集的一种方法
Z1 = np.random.randint(0,10,10)
Z2 = np.random.randint(0,10,10)
print(np.intersect1d(Z1,Z2))

# 使用五种不同的方法去提取一个随机数组的整数部分
A = np.random.uniform(0,10,10)
print("原始值: ", A)
print ("方法 1: ", A - A%1)
print ("方法 2: ", np.floor(A))#np.floor 返回不大于输入参数的最大整数
print ("方法 3: ", np.ceil(A)-1)#np.ceil 返回输入值的上限
print ("方法 4: ", A.astype(int))
print ("方法 5: ", np.trunc(A))#np.trunc 返回截断值

# 将数组的元素四舍五入
A = np.random.uniform(0,10,10)
print("原始值: ", A)
print("方法1: ", np.around(A))
print("方法2: ",end='')
for i in range(len(A)):
    print(np.ceil(A[i]) if A[i] % 1 > 0.5 else np.ceil(A[i]) - 1,end=' ')
print('\n')

# 创建一个 5x5 的矩阵，其中每行的数值范围从 1 到 5
print("方法1:",end='')
A = np.zeros((5,5))
A += np.arange(1,6)
print(A)
print('\n')
print("方法2:",end='')
A = np.zeros((5,5))
for i in range(len(A)):
    A[i,:] = np.arange(1,6)
print(A)

# 创建一个长度为 5 的等间隔一维数组，其值域范围从 0 到 1，但是不包括 0 和 1，使用endpoint=False即不显示最后一个元素
A = np.linspace(0,1,num=6,endpoint=False)[1:]
print(A)

# 创建一个 3x3 的二维数组，并将列按升序排序axis=0，按行则axis=1
A = np.array([[7,4,3],[3,1,2],[4,2,6]])
print("原始数组: \n", A)
A.sort(axis=0)
print(A)

# 从随机一维数组中找出距离给定数值（0.5）最近的数
Z = np.random.uniform(0,1,20)
print("随机数组: \n", Z)
z = 0.5
m = Z.flat[np.abs(Z - z).argmin()]
print(m)

# 找出随机一维数组中出现频率最高的值
# np.bincount()：统计次数，返回的是min-max的次数，用argmax返回最高值的（下标）=对应数值
A = np.random.randint(0,10,20)
print("随机一维数组:", A)
print(np.bincount(A))
print(np.bincount(A).argmax())

# 将二维数组的第一行和第三行进行顺序交换
A = np.arange(25).reshape(5,5)
print(A)
A[[0,2]] = A[[2,0]]
print(A)

# 找出给定一维数组中非 0 元素的位置索引
print(np.nonzero([1,0,2,0,1,0,4,0]))

# 对于随机的 3x3 二维数组，减去数组每一行的平均值
X = np.random.rand(3, 3)
print(X)
Y = X - X.mean(axis=1, keepdims=True)
print(Y)

# 对于给定的 5x5 二维数组，在其内部随机放置 p 个值为 1 的数
p = 5
Z = np.zeros((5,5))
X = np.put(Z, np.random.choice(range(5*5), p, replace=False),1)
print(Z)

# 使用 NumPy 打印昨天、今天、明天的日期
yesterday = np.datetime64('today', 'D') - np.timedelta64(1, 'D')
today     = np.datetime64('today', 'D')
tomorrow  = np.datetime64('today', 'D') + np.timedelta64(1, 'D')
print("yesterday: ", yesterday)
print("today: ", today)
print("tomorrow: ", tomorrow)

# 获得二维数组点积结果的对角线数组
A = np.random.uniform(0,1,(3,3))
B = np.random.uniform(0,1,(3,3))
# 较慢的方法
C = np.diag(np.dot(A, B))
# 较快的方法
C = np.sum(A * B.T, axis=1)
# 更快的方法
C = np.einsum("ij, ji->i", A, B)
print(C)

# 使用 NumPy 按列连接两个数组（要求列数一致）
M1 = np.array([1, 2, 3])
M2 = np.array([4, 5, 6])
MM = np.c_[M1, M2]

# 使用 NumPy 按行连接两个数组（要求行数一致）
M1 = np.array([1, 2, 3])
M2 = np.array([4, 5, 6])
MM = np.r_[M1, M2]

# 将 Ndarray 相邻元素依次累加
Z = np.random.randint(1,10,10)
print(np.cumsum(Z))

# 计算 Ndarray 两相邻元素差值 / N阶差分
Z = np.random.randint(1,10,10)
# 一阶差分：计算 Z 两相邻元素差值
print(np.diff(Z, n=1))
# 二阶差分
print(np.diff(Z, n=2))
# 三阶差分
print(np.diff(Z, n=3))

# 找到随机一维数组中前 p 个最大值
Z = np.random.randint(1,100,100)
p = 5
ZMAX = Z[np.argsort(Z)[-p:]]
print(ZMAX)

# 对于二维随机数组中各元素，保留其 2 位小数
Z = np.random.random((5,5))
print(np.set_printoptions(precision=2))

# 使用科学记数法输出 NumPy 数组
Z = np.random.random([5,5])
print(Z/1e3)

# 找出百分位数（25%，50%，75%）
a = np.arange(15)
print(np.percentile(a, q=[25, 50, 75]))

# 找出数组中缺失值的总数及所在位置
Z = np.random.rand(10,10)
Z[np.random.randint(10, size=5), np.random.randint(10, size=5)] = np.nan
print("缺失值总数: \n", np.isnan(Z).sum())
print("缺失值索引: \n", np.where(np.isnan(Z)))

# 得到二维随机数组各行的最大值
Z = np.random.randint(1,100, [5,5])
print(np.amax(Z, axis=1))

# 计算变量之间的相关系数
Z = np.array([
    [1, 2, 1, 9, 10, 3, 2, 6, 7], # 特征 A
    [2, 1, 8, 3, 7, 5, 10, 7, 2], # 特征 B
    [2, 1, 1, 8, 9, 4, 3, 5, 7]]) # 特征 C
print(np.corrcoef(Z))

# 计算矩阵的特征值和特征向量
# w 对应特征值，v 对应特征向量
M = np.matrix([[1,2,3], [4,5,6], [7,8,9]])
w, v = np.linalg.eig(M)
print(w,v)

# 使用 NumPy 打印九九乘法表
print(np.fromfunction(lambda i, j: (i + 1) * (j + 1), (9, 9)))
