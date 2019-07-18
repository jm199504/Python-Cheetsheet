# 创建tuple
t1 = (1,2,3)
# 访问元组
print(t1[0])
# 连接多个元组
t2 = (4,5,6)
print(t1+t2)
# 删除元组
del t2
# 截取元组(-2表示倒数第二个元素下标)
print(t1[:-2])
# 返回长度
print(len(t1))

# 创建命名元组
from collections import namedtuple
SCU = namedtuple('Master','name age grade')
# 是不是感觉有点像C的结构体/Java的一个实例对象
Jim = SCU(name='Jim',age=23, grade=2)
print('This student is %s, %s years, and grade is %s'%Jim)
# Output:This student is Jim, 23 years, and grade is 2
