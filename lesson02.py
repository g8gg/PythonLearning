# Lesson 02
# Python Coding Structure (Styling)
# Python Features

a = True
if a:
    print(1)
elif a:  # skipped
    print(2)
else:
    print(3)

x = 10
print(1 < 2 < 3 < 4 < x < 100 < 999)
print()
x = None
print(x == True)
print(x == False)
if x:
    print('None→True')
else:
    print('None→False')
print('*' * 10)
print(0 and True)
print('' and True)
print(0.0 and True)
print([] and True)
print({} and True)
print(set() and True)
print('*' * 10)
if 0:
    print('0→True')
else:
    print('0→False')

if 0.0:
    print('0.0→True')
else:
    print('0.0→False')

if '':
    print('\' \'→True')
else:
    print('\' \'→False')

if []:
    print('[]→True')
else:
    print('[]→False')

if {}:
    print('{}→True')
else:
    print('{}→False')

if set():
    print('set()→True')
else:
    print('set()→False')

# While
count = 1
while count <= 5:
    print(count)
    count += 1

# while True:
#     stuff = input("String to capitalize [type q to quit]:")
#     if stuff == 'q':
#         break
#     print(stuff.capitalize())

# while True:
#     value = input("Integer, please [type q to quit]:")
#     if value == 'q':
#         break
#     number = int(value)
#     if number % 2 == 0:
#         continue
#     print(number, "squared is", number * number)

# While else !
count = 1
while count < 6:
    count += 1
else:
    print("while do nothing")

count = 1
while count < 6:
    if count % 2 == 0:
        print("while do something")
        break  # if break while, then execute ELSE
    count += 1
else:
    print("while do nothing")

a = [1, 2, 3]
for i in a:
    if i >= 3:  # u can try `i > 3`
        print("for do something")
        break  # if break for, then execute ELSE
else:
    print("for do nothing")

# for zip()
working_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
fruits = ['banana', 'apple', 'orange', 'pear', 'peach', 'water melon']
drinks = ['coffee', 'tea', 'bear', 'orange juice', 'apple juice', 'cola']
for day, fruit, drink in zip(working_days, fruits, drinks):  # 并行迭代
    print(day, ": drink", drink, "- eat", fruit)

# zip to match 2 lists
days = ['Monday', 'Tuesday', 'Wednesday']
french = ['Lundi', 'Mardi', 'Mercredi']
print(list(zip(days, french)))

# zip to match dictionary
print(dict(zip(days, french)))

# 自然数列 range()
for x in range(0, 10, 2):
    print(x)
for x in range(2, -2, -1):
    print(x)

# 推导式, Python的典型风格 iterable
number_list = []
for number in range(0, 6):
    number_list.append(number)
print(number_list)

number_list = list(range(0, 10))
print(number_list)

# 请理解
number_list = [number for number in range(0, 6)]
print(number_list)

number_list = [number ** 2 for number in range(0, 6)]
print(number_list)

print("*" * 80)
a_list = [number for number in range(0, 6) if number % 2 == 1]
print(a_list)
print("*" * 80)
# 推导的优势: 对Tuple的拆封
# a 3x3 matrix
rows = range(1, 4)
cols = range(1, 4)
cells = [(row, col) for row in rows for col in cols]
for cell in cells:
    print(cell)

cells_row2 = [(row, col) for row in rows if row == 2 for col in cols]
print(cells_row2)

cells_col3 = [(row, col) for row in rows for col in cols if col == 3]
print(cells_col3)

# just remember join()
sep = "→"
a = sep.join(['a', 'b', 'c'])
print(a)

# coming from SuperMan and I crash him.
print([(x, y) for x in range(10) if x % 2 if x > 3 for y in range(10) if y > 7 if y != 8])

word = "我是锅巴GG"
letter_counts = {letter: word.count(letter) for letter in set(word)}  # 字典推导
print(letter_counts)

a_set = {number for number in range(1, 9) if number % 3 == 1}  # 集合推导
print(a_set)

# !!! 元组Tuple是没有推导式的
a = (number for number in range(0, 6))
print(a)  # <generator object <genexpr> at 0x101385a40>

# 生成器推导式
# 是的,没错,圆括号()之间的不是元组推导,而是生成器推导式
number_thing = (number for number in range(0, 6))
print(type(number_thing))
# 直接对生成器对象进行迭代
for number in number_thing:
    print(number)
number_list = list(number_thing)
print(number_list)  # yes, it's empty, coz U can only using it once.
print(type(number_thing))  # right Type
print(number_thing)  # right obj
print("*" * 80)
number_thing = (number for number in range(0, 6))
number_list = list(number_thing)
print(number_list)  # again


def test():
    pass


def agree():
    return True


test()  # do nothing, default return None
print(test() is None)

if agree():
    print('Yes')


def is_none(stuff):
    if stuff is None:
        return "Yes"
    elif stuff:
        return "True"
    else:
        return "False"


print("*" * 80)
print(is_none(None))
print(is_none([]))
print(is_none(()))
print(is_none({}))
print(is_none(0))
print(is_none(1))


def buggy(arg, result=[]):
    result.append(arg)
    print(result)


buggy('a')
buggy('b')  # faint, last returned value keep exist!


def non_buggy(arg, result=None):
    if result is None:
        result = []
    result.append(arg)
    print(result)


non_buggy('a')
non_buggy('b')


def print_args(*args):
    """just test *args positional arguments"""
    print(args)


def print_kwargs(**kwargs):
    print(kwargs)


def print_args_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)


print("*" * 8)
help(print_args)
print(print_args.__doc__)
print_args(1, 2, 3, [1, 2, 3], (1, 2, 3), {1, 2, 3},
           {'1': 2, '2': 4, '3': 6})  # , a="a", b="b", c="c" *只支持位置参数,不支持关键字参数
print("*" * 8)
print_kwargs(a="a", b="b",
             c="c")  # **只支持关键字参数,不支持位置参数 ,1, 2, 3, [1, 2, 3], (1, 2, 3), {1, 2, 3}, {'1': 2, '2': 4, '3': 6}
print("*" * 8)
print_args_kwargs(1, 2, 3, [1, 2, 3], (1, 2, 3), {1, 2, 3},
                  {'1': 2, '2': 4, '3': 6}, a="a", b="b", c="c")  # right solution, 位置参数before关键字参数
