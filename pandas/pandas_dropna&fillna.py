import pandas as pd
import numpy as np

dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),
                  index=dates, columns=['A','B','C','D'])
df.iloc[0,1] = np.nan
df.iloc[1,2] = np.nan
print(df)

# 使用dropna删除NaN
# axis=0为对行进行操作，1对列进行操作
# how='any'只要存在NaN就drop，'all'必须全部为NaN才drop
df1=df.dropna(axis=0,how='all')
print(df1)

# 使用pd.fillna()可以使用其他值替代NaN
df2=df.fillna(value=0)
print(df2)

# 使用pd.isnull()来判断是否存在有缺失数据NaN,True为缺失值NaN
print(df.isnull())
