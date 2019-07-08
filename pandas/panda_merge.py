import pandas as pd

#定义资料集
left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})

#依据key横向合并
res = pd.merge(left, right, on='key')

print(res)

#定义资料集
left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                      'key2': ['K0', 'K1', 'K0', 'K1'],
                      'A': ['A0', 'A1', 'A2', 'A3'],
                      'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                       'key2': ['K0', 'K0', 'K0', 'K0'],
                       'C': ['C0', 'C1', 'C2', 'C3'],
                       'D': ['D0', 'D1', 'D2', 'D3']})

#依据key1与key2 columns进行合并，并打印出四种结果['left', 'right', 'outer', 'inner']
res = pd.merge(left, right, on=['key1', 'key2'], how='inner')
print(res)

res = pd.merge(left, right, on=['key1', 'key2'], how='outer')
print(res)

res = pd.merge(left, right, on=['key1', 'key2'], how='left')
print(res)

res = pd.merge(left, right, on=['key1', 'key2'], how='right')
print(res)

#定义资料集
df1 = pd.DataFrame({'col1':[0,1], 'col_left':['a','b']})
df2 = pd.DataFrame({'col1':[1,2,2],'col_right':[2,2,2]})

# 依据col1进行合并，并启用indicator=True
res = pd.merge(df1, df2, on='col1', how='outer', indicator=True)
print(res)

# 自定indicator column的名称
res = pd.merge(df1, df2, on='col1', how='outer', indicator='indicator_column')
print(res)