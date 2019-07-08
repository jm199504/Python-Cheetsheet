# list特征1：append()添加元素
list1 = [1,2,3]
list1.append(4)
print(list1)
# Output:[1, 2, 3, 4]

# list特征2：del（)删除
del list1[2]
print(list1)
# Output:[1, 2, 4]

# list特征3：+相加
list2 = [0,1,2]
list3 = list1 + list2
print(list3)
# Output:[1, 2, 4, 0, 1, 2]

# list特征4：len()获取长度
print(len(list3))
# Output:6

# list特征5：in包含
print(5 in list3)
# Output: False

# list特征6：max()极值
print(max(list1))
# Output:4

# list特征7：sort()排序
list3.sort()
print(list3)
# Output:[0, 1, 1, 2, 2, 4]

# ======程序员专用分割线======
from collections import deque
# 创建deque
d1 = deque([1,3,2,4])
d2 = deque('abcdef')

# deque特征1：append()
d1.append(5)
print(d1)
# Output:deque([1, 3, 2, 4, 5])
d2.append('g')
print(d2)
# Output:deque(['a', 'b', 'c', 'd', 'e', 'f', 'g'])

# deque特征2：pop()返回结尾元素且删除
print(d2.pop())
# Output:g
print(d2)
# Ouptput:deque(['a', 'b', 'c', 'd', 'e', 'f'])

# deque特征3：extend()
d3 = deque([9,9])
d3.extend(d1)
print(d3)
# Output:deque([9, 9, 1, 3, 2, 4, 5])

# deque特征4：insert()
d3.insert(0,10)
print(d3)
# Output:deque([10, 9, 9, 1, 3, 2, 4, 5])

# deque特征5：clear()
d3.clear()
print(d3)
# Output:deque([])

# deque特征6：reverse()
d1.reverse()
print(d1)
# Output:deque([5, 4, 2, 3, 1])
