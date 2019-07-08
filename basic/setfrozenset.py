# set特性1不存在重复值
s1 = {1,1,2,3,4}
# print(s1)
# Output:{1, 2, 3, 4}

# set特征2访问是无序的,不支持通过索引访问集合元素
# set特征3是可变的，支持加入不同类型的元素，同时发现加入字符串输出时在第一个，也证明了无序性

s1.add('python')
# print(s1)
# Output:{'python', 1, 2, 3, 4}

# set特征3：续-但是不能向set中加入可变容器例如列表、字典-->会报错unhashable type:‘list’
# s1.add([1,2])
# print(s1)
# Output:TypeError: unhashable type: 'list'

# set特征4：update(item) 注意这里的update不再是更新修改，而是将item拆分后多个子元素加入集合
s1.update('hi')
# print(s1)
# Output:{1, 2, 3, 4, 'h', 'python', 'i'}

# set特征5：remove(item)移除操作，需要注意当你移除不存在的元素会报错KeyError
s1.remove('h')
# print(s1)
# Output:{1, 2, 3, 4, 'python', 'i'}
# s1.remove(100)
# print(s1)
# Output:KeyError: 100

# set特征6：union(联合), intersection(交集), difference(差集)和sysmmetric difference(对称差集)
s1 = {6,4,3,4,5}
s2 = {1,2,3,7,4}
# 求交集操作，选取s1和s2都存在的元素
s3 = s1 & s2
# 求并集操作，选取s1和s2中全部元素
s4 = s1 | s2
# 求差集操作，将去除s1中在s2也存在的元素
s5 = s1 - s2
# 与非操作，将在两个set中均存在的元素去除
s6 = s1^s2
# =====程序员专用分割线=====
# frozenset冻结的集合，冻结后不能再添加或者删除元素,注意添加/移除元素要报错
fs1 = frozenset({1,1,2,3,4})
print(fs1)