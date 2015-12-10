# Lesson 03
# in Python world, everything is object, The first class citizen should be function
# so, let's learning function


def my_func():
    """我的测试函数"""
    print("my_func be called.")


help(my_func)
print(my_func.__doc__)
print("*" * 80)


def run_func(func):
    func()  # just run function passed by function name argument


def run_calc_func(func, *args):
    """
    传入计算函数,计算后续数列,并打印值
    :param func:
    :param args:
    :return: func(args)
    """
    return func(args)


run_func(my_func)

print(run_calc_func(sum, 1, 2, 3))
print(run_calc_func(min, 10, 21, 3))


# inner function
def my_quote(saying):
    def inner(quote):
        return "G8GG says: '%s'" % quote

    return inner(saying)


print(my_quote("不错"))


# closure 闭包
def my_quote2(saying):
    def inner2():
        return "G8GG says: '%s'" % saying  # 闭包可改变和存储函数外创建的值

    return inner2  # 返回闭包,同时TA也是函数


a = my_quote2("闭包不错")
print(type(a))  # 闭包就是函数
print(a)  # 动态创建的可以记录外部变量的函数
print(a())  # 调用看看


# 匿名函数: lambda()
def edit_story(words, func):
    for word in words:
        print(func(word))


stairs = ['thud', 'meow', 'thud', 'hiss']


def enliven(word):
    return word.capitalize() + '!'


edit_story(stairs, enliven)
print("*" * 80)
edit_story(stairs, lambda word: word.capitalize() + '!')  # Lambda


# 生成器/generator
def my_range(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number
        number += step


ranger = my_range(1, 5)
print(type(ranger))
for x in ranger:
    print(x)

print('*' * 80)


# Decorator 装饰器
# 不改变源代码的情况下修改已经存在的函数
# 装饰器本质上是一个函数,它把一个函数作为输入并且返回另外一个函数

def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        result += result
        return result

    return new_function  # return closure


def add_ints(a, b):
    return a + b


print(add_ints(3, 5))

cooler_add_ints = document_it(add_ints)  # 对装饰器赋值
cooler_add_ints(3, 5)


# 需要装饰的函数前,可以直接添加装饰器名字,代替装饰器赋值的代替
@document_it
def add_ints(a, b):
    return a + b


add_ints(3, 5)


# 同样一个函数可以有多个装饰器
def square_it(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result

    return new_function


@document_it
@square_it
def add_ints(c, d):
    return c + d


print("*" * 70)
print(add_ints(3, 5))


@square_it
@document_it
def add_ints2(e, f):
    return e + f


print("*" * 60)
print(add_ints2(3, 5))

# 离被装饰的函数最近的装饰器,最先被执行,并依次执行上面的装饰器
# 但是,任何顺序,装饰的最终结果是一致的 (此句原书翻译错误)
# fixed: 当然结果和装饰顺序有关,我改了例子,已经证明了这一点
ß
