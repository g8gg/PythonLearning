# import from package
# learning std lib
# counter/ordered etc...
# iterator & tools

from boxes.sources import daily, weekly
from collections import Counter
from collections import OrderedDict  # 按序添加
from pprint import pprint
import itertools

print('Daily forecast:', daily.forecase())
print('Weekly forecast:', weekly.forecase())

breakfast = ['eggs', 'spam', 'spam', 'spam']
breakfast_count = Counter(breakfast)
lunch = ['eggs', 'bacon', 'eggs']
lunch_count = Counter(lunch)
print(breakfast_count)
print(lunch_count)
print(breakfast_count.most_common())  # 降序
print(lunch_count.most_common())  # 降序

print("*" * 30)
print(breakfast_count + lunch_count)
print(breakfast_count - lunch_count)
print(lunch_count - breakfast_count)
print("*" * 20)
print(breakfast_count | lunch_count)
print(breakfast_count & lunch_count)

print()
quote = {'a': 'A wise guy, huh?', 'Larry': 'Ow!', 'Curly': 'Nyuk nyuk!', 'Turly': 'Lol!'}
quotes = OrderedDict([('a', 'A wise guy, huh?'), ('Larry', 'Ow!'), ('Curly', 'Nyuk nyuk!'), ('Turly', 'Lol!')])

pprint(quotes)
for stooge in quote:  # not sorted 无序
    print(stooge)

print("-" * 80)
for stooge in quotes:  # ordered 按插入顺序
    print(stooge)


# 双端队列: 栈+队列
def palindrome(word):
    from collections import deque
    dq = deque(word)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True


print("回文判断,是否对称")
print(palindrome('a'))
print(palindrome('aba'))
print(palindrome('abba'))
print(palindrome('abca'))


def another_palindrome(word):
    """字符串反转比较"""
    print(word, word[::-1])
    return word == word[::-1]


print("回文判断,是否对称")
print(another_palindrome('a'))
print(another_palindrome('aba'))
print(another_palindrome('abba'))
print(another_palindrome('abca'))

for item in itertools.chain([1, 2], ['a', 'b'], (3, 4), {5, 6}, {"g8": "gg", "G8": "GG"}):
    print(item)

count = 0
for item in itertools.cycle([1, 2]):
    print(item)
    count += 1
    if count >= 10:
        break


def multiply(a, b):
    return a * b


for item in itertools.accumulate([1, 2, 3, 4], multiply):
    print(item)

for item in itertools.accumulate([1, 2, 3, 4], lambda x, y: x * y):
    print(item)
