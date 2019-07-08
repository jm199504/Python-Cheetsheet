# 创建dict字典
dict1 = {'A': '11', 'B': '22', 'C': '33'}
# dict特征1：根据key获取value
print(dict1['B'])

# dict特征2：修改value
dict1['A'] = 11
print(dict1)

# dict特征3：del删除
del dict1['C']
print(dict1)

# dict特征4：clear清空
# dict1.clear()
# print(dict1)

# dict特征5：加入新的元素
dict1['C'] = 33
print(dict1)

# 创建defaultdict
from collections import defaultdict
df1 = defaultdict(int)
df2 = defaultdict(set)
df3 = defaultdict(str)
df4 = defaultdict(list)
# 访问不存在的key值并不会报错而是返回默认类型初始值
print(df1[1],df2[1],df3[1],df4[1])
# Output:0 set()  []

# OrderedDict创建
from collections import OrderedDict
od1 = OrderedDict()
od1['A'] = 1
od1['B'] = 2
od1['C'] = 3
print(od1)
# Output:OrderedDict([('A', 1), ('B', 2), ('C', 3)])
# 与普通字典dict作对比
d2 = dict()
d2['A'] = 1
d2['B'] = 2
d2['C'] = 3
print(d2)
# Output:{'B': 2, 'C': 3, 'A': 1}

# 创建Counter
from collections import Counter
s = 'hello'
c = Counter(s)
print(c)
# Output: Counter({'l': 2, 'e': 1, 'o': 1, 'h': 1})

