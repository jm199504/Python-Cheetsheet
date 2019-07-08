import collections

print(isinstance(list(), collections.Iterable))
# Output：True   说明列表是一个可迭代对象

print(isinstance(dict(), collections.Iterable))
# Output：True   说明字典是一个可迭代对象

print(isinstance(iter(list()), collections.Iterator))
# Output: True  使用iter()定义一个迭代器，注意()中必须填写list()等可迭代对象

print(isinstance(iter([]), collections.Iterable))
# Output: True  显然一个迭代器也是一个可迭代对象

print(isinstance([], collections.Iterator))
# Output：False  可迭代对象不一定是迭代器

print(isinstance((x * x for x in range(10)), collections.Iterable))
# Output：True   如定义所述的可使用for循环的对象都是可迭代对象

iter1 = iter([1,2])
print(iter1.__next__())
# Output：1
print(iter1.__next__())
# Output：2
print(iter1.__next__())
# Output：StopIteration