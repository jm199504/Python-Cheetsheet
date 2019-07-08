import pandas as pd
import numpy as np

#定义资料集
df1 = pd.DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'])
df2 = pd.DataFrame(np.ones((3,4))*1, columns=['a','b','c','d'])
df3 = pd.DataFrame(np.ones((3,4))*2, columns=['a','b','c','d'])

#concat纵向合并 axis=0纵向，axis=1横向
res = pd.concat([df1, df2, df3], axis=1)

#打印结果
print(res)

#将index_ignore设定为True，序号升序显示(index从0-8)
res = pd.concat([df1, df2, df3], axis=0, ignore_index=True)

#打印结果
print(res)

#定义资料集
df1 = pd.DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'], index=[1,2,3])
df2 = pd.DataFrame(np.ones((3,4))*1, columns=['b','c','d','e'], index=[2,3,4])

#纵向"外"合并df1与df2，默认join为outer，即相同的column才合并，不同则NaN
res = pd.concat([df1, df2], axis=0,join='outer')

#打印结果
print(res)

#纵向"内"合并df1与df2,当join为inner时column不同的数据将会被丢弃
res = pd.concat([df1, df2], axis=0, join='inner')

#打印结果
print(res)

#定义资料集
df1 = pd.DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'])
df2 = pd.DataFrame(np.ones((3,4))*1, columns=['a','b','c','d'])
df3 = pd.DataFrame(np.ones((3,4))*1, columns=['a','b','c','d'])
s1 = pd.Series([1,2,3,4], index=['a','b','c','d'])

#将df2合并到df1的下面，以及重置index，并打印出结果
res = df1.append(df2, ignore_index=True)#注意append仅能纵向合并
print(res)

#合并多个df，将df2与df3合并至df1的下面，以及重置index，并打印出结果
res = df1.append([df2, df3], ignore_index=True)
print(res)

#合并series，将s1合并至df1，以及重置index，并打印出结果
res = df1.append(s1, ignore_index=True)
print(res)