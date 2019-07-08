import numpy as np

#查看numpy的版本
print(np.__version__)

#创建一维数组
print(np.array([1,2,3]))

#创建二维数组
print(np.array([(1,2,3),(4,5,6)]))

#创建全零数组
print(np.zeros((3,3)))

#创建全一数组
print(np.ones((2,3,4)))

#创建一维等差数组(0 1 2 3 4)
print(np.arange(5))

#创建二维等差数列
print(np.arange(6).reshape(2,3))

#创建单位矩阵（二维数组）
print(np.eye(3,3))

#创建等间隔的一维数组
print(np.linspace(1, 10, num=6))

#创建二维随机数组
print(np.random.rand(2,3))

#创建二维随机整数数组（数值小于 5）
print(np.random.randint(5, size=(2,3)))

#依据自定义函数创建数组
print(np.fromfunction(lambda i, j: i + j, (3, 3)))

#生成二维示例数组（可以看作矩阵）
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])

#矩阵乘法运算
print(np.dot(A, B))

#使用 np.mat 将二维数组准确定义为矩阵，就可以直接使用 * 完成矩阵乘法计算 = np.dot(A,B)
print(np.mat(A) * np.mat(B))

#矩阵的转置
print(A.T)

#矩阵求逆
print(np.linalg.inv(A))

#三角函数
a = np.array([10,20,30,40,50])
print(np.sin(a))

#以自然对数函数为底数的指数函数
print(np.exp(a))

#数组的方根的运算（开平方）
print(np.sqrt(a))

#数组的方根的运算（立方）
print(np.power(a, 3))

#生成一维示例数组[0:1]
a = np.random.random((3, 2))

#更改数组形状（不改变原始数组）
print(a.reshape(2, 3))

#更改数组形状（会改变原始数组）
print(a.resize(2, 3))

#展平数组
print(a.ravel())

a = np.random.randint(10, size=(3, 3))#随机数：0-10
b = np.random.randint(10, size=(3, 3))#随机数：0-10

# 垂直拼合数组
print(np.vstack((a, b)))

#水平拼合数组
print(np.hstack((a, b)))

# 沿纵轴分割数组
print(np.hsplit(a, 3))

# 沿横轴分割数组
print(np.vsplit(a, 3))

# 返回每列最大值
print(np.max(a, axis=0))

# 返回每行最小值
print(np.min(a, axis=1))

# 返回每列最大值索引
print(np.argmax(a, axis=0))

# 统计数组各列的中位数
print(np.median(a, axis=0))

# 数组各行的算术平均值
print(np.mean(a, axis=1))

# 数组各列的加权平均值
print(np.average(a, axis=0))

# 统计数组各行的方差
print(np.var(a, axis=1))

# 统计数组各列的标准偏差
print(np.std(a, axis=0))

#np.random的方法总结
print('==Numpy.random.(*)方法总结==')

# 生成一个[0,1)之间的随机浮点数或N维浮点数组
print(np.random.rand())

#生成生成[0,1)之间随机浮点数
print(np.random.rand())

#生成一个形状为5的一维数组
print(np.random.rand(5))

#生成2x3的二维数组
print(np.random.rand(2,3))

#np.random.rand()  生成一个浮点数或N维浮点数组，取数范围：正态分布的随机样本数
print(np.random.randn())

print(np.random.randn(2,3))

# np.random.standard_normal(size=None)：生成一个浮点数或N维浮点数组，取数范围：标准正态分布随机样本
print(np.random.standard_normal(2))
print(np.random.standard_normal((2,3)))

# np.random.randint(low, high=None, size=None, dtype='l')：
# 生成一个整数或N维整数数组，取数范围：若high不为None时，取[low,high)之间随机整数，否则取值[0,low)之间随机整数。
print(np.random.randint(2))

print(np.random.randint(2,size=5))

print(np.random.randint(2,6,size=5))

# np.random.choice(a, size=None, replace=True, p=None)：
# 从序列中获取元素，若a为整数，元素取值为np.range(a)中随机数；若a为数组，取值为a数组元素中随机元素
print(np.random.choice(2,2))

print(np.random.choice(np.array(['a','b','c','f']),(2,3)))

# np.random.shuffle(x)：对X进行重排序，如果X为多维数组，整行重排
list1 = [1,2,3,4,5]
np.random.shuffle(list1)
print(list1)

# 将[0,1,2,3,4,5,6,7,8]转为[[0,1,2],[3,4,5],[6,7,8]]
arr = np.arange(9).reshape(3,3)
print(arr)

# 打乱arr的元素顺序
np.random.shuffle(arr)
print(arr)

#生成一个range(5)随机顺序的数组
print(np.random.permutation(5))

# 比较：np.random.permutation(x)：与numpy.random.shuffle(x)函数功能相同，两者区别：peumutation(x)不会修改X的顺序