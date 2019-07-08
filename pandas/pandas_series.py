import pandas as pd
import numpy as np

# 1 列表类型
s = pd.Series([1,3,5,np.nan,6,8])
print(s)
# 2 字典类型
s1 = pd.Series({'a':1,'b':2,'c':3})
print(s1)
# 3 字典类型和索引
s11 = pd.Series({'a':1,'b':2,'c':3},index=['a','b','c','d'])
print(s11)
# 4 判断series是否为空
print(pd.isnull(s11))
print(s11.isnull())
print(s11.notnull())
# 5 plus
s = s1+s11
print(s)
# 6 为series和index添加name属性
s1.name = 'population'
s1.index.name = 'state'
print(s1)
# 7 修改索引值
s1.index = ['A','B','C']
# 8 通过values和index属性获取其数组表示形式和索引对象
print(s1.values)
print(s1.index)
# 9 利用索引index获取其value
print(s1['A'])
print(s1[['A','C']])
# 10 根据条件获取value
print('======')
print(s1[s1>1])
# 11 判断索引知否存在
print('a' in s1)
# 12 直接操作value
print(np.exp(s1))
# 13 对所有value添加值
s1 = s1.add(4)
print(s1)



