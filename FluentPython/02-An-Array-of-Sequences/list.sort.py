# list.sort and the sorted Built-In Function
# The list.sort method sorts a list in place — that is, without making a copy.
# 注意哦, 并没有产生任何copy
### 这里体现了一个重要的Python API原则
# It returns None to remind us that it changes the target object, and does not create a new list.
# 如果函数或者方法返回None,说明: 就地改变对象,没有新对象创建
# This is an important Python API convention: functions or methods that change an object in place should return None
#  to make it clear to the caller that the object itself was changed, and no new object was created.
fruits = ['grape', 'raspberry', 'apple', 'banana']
print(fruits)  # old list
print(sorted(fruits))  # new list, fruits not changed
print(fruits)  # old list
print("*" * 80)
print(sorted(fruits, reverse=True))
print(sorted(fruits, key=len))
print(sorted(fruits, key=len, reverse=True))
print("*" * 80)
print(fruits.sort())  # None means in-place/ no new list be created
print(fruits)
