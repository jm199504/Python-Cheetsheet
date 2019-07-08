import tushare as ts

# 获取数据
df = ts.get_k_data('002253')

# 1 汇总统计
print(df.describe())

# 2 非NaN值统计
print(df.count())

# 3 最大值和最小值
print(df.min())
print(df.max())

# 4 最大值和最小值所对应的索引值，由于多维度，不指定具体的属性将会报错
# 另外idxmin/idmax仅返回index的下标
print(df['date'][df['open'].idxmin()])
print(df['open'].idxmax())

# 5 数据集的分位数，默认为0.5 显示2/4分位数
# df.quantile(0.75)，显示3/4分位数
print(df.quantile())
print(df.quantile(0.75))

# 6 列值总和
print(df.sum())

# 7 各列均值
print(df.mean())

# 8 各列中位数
print(df.mean())

# 9 各列根据平均值计算平均绝对离差，即平均绝对误差（Mean Absolute Deviation）
print(df.mad())

# 10 各列方差
print(df.var())

# 11 各列标准差
print(df.std())

# 12 各列偏度，即三阶标准化矩
print(df.skew())

# 13 各列峰度
print(df.kurt())

# 14 各列累加和
print(df.cumsum())

# 15 各列累加和最大值和最小值
print(df.cummin())
print(df.cummax())

# 16 指定列累积
print(df['open'].cumprod())

# 17 一阶方差
print(df['open'].diff())

# 18 各列百分数变化
print(df['open'].pct_change())

# 19 各列协方差
print(df['open'].cov())
