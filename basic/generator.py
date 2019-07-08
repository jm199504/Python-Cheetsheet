import collections

def generator_demo():
    print('输出语句1')
    yield 1
    print('输出语句2')
    yield 2
    print('输出语句3')
    yield 3

gd = generator_demo()
print(isinstance(gd, collections.Iterator))
# Output： True
print(isinstance(gd, collections.Iterable))
# Output： True
print(isinstance(gd, collections.Generator))
# Output： True
print(gd.__next__())
# 执行第一个yield的前面的语句，因此注意不会输出语句2和3
# Output： 输出语句1
# Output： 1
print(gd.__next__())
# Output： 输出语句2
# Output： 2