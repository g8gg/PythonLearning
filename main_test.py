# hello world
import os

# 元组
a = [1, 2, 3, 4, '五']
print(a),
a[0] = '一'
print(a),

for item in a:
    print(item)

# 字典
aDict = {1: 1, 2: 2, 3: 3, 'test': '测试'}
for key in aDict:
    print(key, aDict[key])

# 判断
if 1 < 0:
    print("1")
elif 1 > 0:
    print("2")
else:
    print("cao")

# while
counter = 0
while counter < 3:
    print('*')
    counter += 1

# for
for item in ['①', '②', '③', '④']:
    print(item)
print()

for item in range(10):
    print(item)

foo = "你是不是真的☺☂"
for item in foo:
    print(item)
for i in range(len(foo)):
    print(foo[i], '(%d)' % i)

for i, item in enumerate(foo):
    print(item, '(%d)' % i)

# 列表解析
squared = [x ** 2 for x in range(10)]
for i in squared:
    print(i)

squared = [x ** 2 for x in range(8) if not x % 2]
print(squared)

# file op
# with open('/Users/gosber/test.txt', 'w',encoding='utf-8') as f:
#   print('This will be written to somedir/spamspam.txt测试看看☺', file=f)

print("There are <", 2 ** 32, "> possibilities!", sep=" ", end='')
print(" no RnLF ")

#fileName = input('Enter file name (current path):')
fileName = 'test.txt'
fObj = open(fileName, mode='w+', encoding='utf8')  # rw mode
for i in range(len(foo)):
    print(foo[i], '(%d)' % i, file=fObj)
fObj.seek(0)
for eachLine in fObj:
    print(eachLine)
fObj.close()
