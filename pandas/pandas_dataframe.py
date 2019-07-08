import pandas as pd
import numpy as np

# 1 创建dataframe
d = {'one' : pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
     'two' : pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
df1 = pd.DataFrame(d)
print(df1)

# 2 创建dataframe
df2 = pd.DataFrame({
'A' : 1.,
'B' : pd.Timestamp('20160101'),
'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
'D' : np.array([3] * 4,dtype='int32'),
'E' : pd.Categorical(["test","train","test","train"]),
'F' : 'foo' })
print(df2)

# 3 创建dataframe
dates = pd.date_range('20160101',periods=6)
df3 = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
print(df3)

# 4 创建dataframe
df4 = pd.DataFrame([{'one' : 1,'two':1},{'one' : 2,'two' : 2},{'one' : 3,'two' : 3},{'two' : 4}]
                  ,index=['a','b','c','d'],columns=['one','two'])
df4.index.name='index'
print(df4)

# 5 为不存在的列赋值会创建出一个新列
df4['new_c'] = 666
print(df4)

# 6 关键字del删除列
del df4['new_c']
print(df4)

# 7 查看不同列数据类型
print(df4.dtypes)

# 8 DataFrame转换为其他类型
dict4 = df4.to_dict(orient='dict')
print(dict4)

# 9 获取列数据
print(df4['one'])

# 10 创建数据
dates = pd.date_range('20150101',periods=30)
# index索引为日期，columns列名
df = pd.DataFrame(np.random.randn(30,4),index=dates,columns=list('ABCD'))

# 11 查看前5行和后3行数据
print(df.head())
print(df.tail(3))

# 12 查看索引值/列名/values
print(df.index)
print(df.columns)
print(df.values)

# 13 进行快速统计
print(df.describe())

# 14 对数据转置
df.T

# 15 对列名进行排序/对值排序
print(df.sort_index(axis=1, ascending=False))

# 16 对指定列及按值进行排序
print(df.sort_values(by='A'))
print(df.head().sort(columns='B'))

# 17 查看数据形状
print(df.shape)

# 18 查看数据总数
print(df.size)

# 19 查看指定列/行
print(df['A'])
print(df.A)
print(df[0:3])

# 20 根据标签选取数据   df.loc[行标签,列标签]
print(df.loc['2015-01-02':'2015-01-04','A':'C'])

# 21 根据位置选取数据   df.iloc[行位置,列位置]
print(df.iloc[0:2,:])   #选取第一行到第三行（不包含）的数据
''' PS：loc为location的缩写，iloc则为integer & location的缩写 '''

# 22 条件选择数据(布尔索引)
print(df[df.A >= 1])
print(df[df>=1])

# 23 使用isin()方法过滤
# 对df进行添加新的列
df['E']=['one', 'one','two','three','four']*6
print(df)
print(df[df['E'].isin(['two','four'])])

















