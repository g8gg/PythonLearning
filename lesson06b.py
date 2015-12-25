# Object & Class
# Lesson 06 b
# Class method &  Static method
# Polymorphic
# named tuple 命名元组
from collections import namedtuple
from this import s
import codecs

print('rot-13', "-" * 70)
print(s)  # rot13 encoding !
print("-" * 80)
print(codecs.decode(s, "rot-13"))


class A:
    count = 0

    def __init__(self):
        A.count += 1

    def exclaim(self):
        print('I\'m an A!')

    @classmethod
    def kids(cls):
        print("A has", cls.count, "little objects.")


easy_a = A()
easy_b = A()
easy_c = A()
easy_d = A()
easy_a.count = 0
easy_b.count = 1
easy_c.count = 2
easy_d.count = 3
print(easy_a.count)
print(easy_b.count)
print(easy_c.count)
print(easy_d.count)
print(A.count)
# Class Method (keep class attribute)
# A.count = cls.count, not the self.count (instance attribute)
easy_a.kids()
easy_b.kids()
easy_c.kids()
easy_d.kids()
A.kids()


# Static Method
class CoyoteWeapon:
    @staticmethod  # 静态方法只是属于类的定义,不属于类(Class or cls)也不属于实例
    def commercial():  # no self, no everything
        print('This CoyoteWeapon has been brought to you by Acme')


CoyoteWeapon.commercial()


# Duck Typing
class Quote:
    def __init__(self, person, words):
        self.person = person
        self.words = words

    def who(self):
        return self.person

    def says(self):
        return self.words + '.'


class QuestionQuote(Quote):
    def says(self):
        return self.words + '?'


class ExclamationQuote(Quote):
    def says(self):
        return self.words + '!'


hunter = Quote('G8GG', 'Python is good')
print(hunter.who(), 'says:', hunter.says())
hunted = QuestionQuote('Bugs Bunny', 'What\'s up, dc')
print(hunted.who(), 'says:', hunted.says())
hunted1 = ExclamationQuote('Daffy Duck', 'It\'s rabbit season')
print(hunted1.who(), 'says:', hunted1.says())

print('-' * 80)


# 多态
# 面向对象的三大特性：封装、继承、多态
# 从一定角度来看，封装和继承几乎都是为多态而准备的
# 多态存在的三个必要条件
#   一、要有继承；
#   二、要有重写；
#   三、父类引用指向子类对象
# 实现多态的技术称为：动态绑定（dynamic binding），是指在执行期间判断所引用对象的实际类型，根据其实际的类型调用其相应的方法
# 多态的作用：消除类型之间的耦合关系

def who_says(obj):  # Duck Typing
    print(obj.who(), 'says', obj.says())


who_says(hunter)
who_says(hunted)
who_says(hunted1)


# magic method / special method
class Word:
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text

    def __repr__(self):
        return 'Word→' + self.text


first = Word('Majun')
print(first)  # use __str__

""" Run in Python Console
>>> class Word:
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text

    def __repr__(self):
        return 'Word→' + self.text
>>> first = Word('test')
>>> first  # use __repr__
Word→test
"""

print("-" * 80)


# Class and Named Tuple

# class
# is-a关系用继承, has-a关系考虑组合(composition)和聚合(aggregation)


class Bill:
    def __init__(self, description):
        self.description = description


class Tail:
    def __init__(self, length):
        self.length = length


class Duck:
    def __init__(self, bill, tail):
        self.bill = bill
        self.tail = tail

    def about(self):
        print('This duck has a', self.bill.description, 'bill and a', self.tail.length, 'tail')


tail = Tail('long')
bill = Bill('wide orange')
duck = Duck(bill, tail)
duck.about()

# named tuple
# 命名元组的使用,三种初始化方法
Duck1 = namedtuple('Duck', 'bill tail')
duck1 = Duck1('wide orange', 'long')
print(duck1)
print(duck1.bill, duck1.tail)

# named tuple constructed by dictionary {}
parts = {'bill': 'wide orange', 'tail': 'long'}  # **parts是关键词变量(keyword argument),抽取出key-value供Duck1()使用
duck2 = Duck1(**parts)
print(duck2)
# print(duck2.bill, duck2.tail)
duck3 = Duck1(bill='wide orange 3', tail='long 3')  # 作用同上
print(duck3)
# print(duck3.bill, duck3.tail)

# 命名元组是不可变的,但是可以修改某些域的值并返回一个新的命名元组,不同于字典Dict
duck_dict = {'bill': 'wide orange', 'tail': 'long'}
duck_dict['color'] = 'red'  # dict add new K-V pair
print(duck_dict)

# duck3.bill='test'  # can't set attribute
duck4 = duck1._replace(bill='crushing', tail='magnificent')
print(duck4)
# duck4.color="red"  # AttributeError: 'Duck' object has no attribute 'color'



# 命名元组的好处
Settings = namedtuple('App', 'AppName Version Author MD5Sign Major Minor Build')
my_app_settings = Settings('App1', '1.0', 'G8GG', 'xxxxxxxxxx', '1', '01', '1212')
print(my_app_settings.AppName)

Settings.AppName = "App2"
# Settings.
print(my_app_settings.AppName)

Point = namedtuple('Point', ['x', 'y'])
p = Point(11, y=12)
print(p)
x, y = p
print(x, y)

a = [{"a": "a"}, {"bb": 1}]
# print(a.)

import pandas as pd

# import numpy as np

tmp = pd.DataFrame(a)
# tmp.
