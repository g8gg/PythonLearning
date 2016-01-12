# Using + and * with Sequences
# Both + and * always create a new object, and never change their operands.
print('*' * 20 + ' Using + and * with Sequences ' + '*' * 20)
l = [1, 2, 3]
print(l * 5)
print(5 * 'abcd ')

# 当心
# will result in a list with three references to the same inner list, which is probably not what you want.
my_list = [[]] * 3
print(my_list)
my_list[0] = list(range(0, 3))
my_list[1] = list(range(3, 6))
my_list[2] = list(range(6, 9))
print(my_list)

# Building Lists of Lists
print('*' * 20 + ' Building Lists of Lists ' + '*' * 20)
# Sometimes we need to initialize a list with a certain number of nested lists

# A list with three lists of length 3 can represent a tic-tac-toe board
board = [['_'] * 3 for i in range(3)]  # Create a list of three lists of three items each. Inspect the structure.
print(board)
board[1][2] = 'X'  # Place a mark in row 1, column 2, and check the result.
print(board)

# A tempting but wrong shortcut is doing it like this:
weird_board = [[
                   '_'] * 3] * 3  # The outer list is made of three references to the same inner list. While it is unchanged, all seems right.
print(weird_board)
# 给你看看鬼片
# Placing a mark in row 1, column 2, reveals that all rows are aliases referring to the same object.
weird_board[1][2] = 'O'  # A list with three references to the same list is useless
print(weird_board)
# The problem in essence, it behaves like this code:
row = ['_'] * 3
board = []
for i in range(3):
    board.append(row)
# The same row is appended three times to board.
print(board)
row[0] = 'x'
print(board)
board[0][2] = 'O'
print(board)
print(row)

# On the other hand, the list comprehension from above is equivalent to this code:
print('')
board = []
for i in range(3):
    row = ['_'] * 3  # Each iteration builds a new row and appends it to board.
    board.append(row)
print(board)
board[2][0] = 'O'  # Only row 2 is changed, as expected.
print(board)

# 还有更烧脑的呢
# there are also the += and *= operators, which produce very different results
# depending on the mutability of the target sequence.

### Augmented Assignment with Sequences
print('*' * 20 + ' Augmented Assignment with Sequences ' + '*' * 20)
# The augmented assignment operators += and *= behave very differently depending on the first operand.
# o simplify the discussion, we will focus on augmented addition first (+=),
# but the concepts also apply to *= and to other augmented assignment operators.
# The special method that makes += work is __iadd__ (for “in-place addition”).
#  However, if __iadd__ is not implemented, Python falls back to calling __add__. Consider this simple expression:
# >>> a += b
# If a implements __iadd__, that will be called. In the case of mutable sequences
# (e.g., list, bytearray, array.array), a will be changed in place (i.e., the effect will be similar to a.extend(b)).
# However, when a does not implement __iadd__, the expression a += b has the same effect as a = a + b:
# the expression a + b is evaluated first, producing a new object, which is then bound to a.
# In other words, the identity of the object bound to a may or may not change, depending on the availability of __iadd__.
# In general, for mutable sequences, it is a good bet that __iadd__ is implemented and that += happens in place.
#  For immutable sequences, clearly there is no way for that to happen.
# What I just wrote about += also applies to *=, which is implemented via __imul__.

# Here is a demonstration of *= with a mutable sequence and then an immutable one:
l = [1, 2, 3]
print(type(l))
print(id(l))  # ID of the initial list
l *= 2
print(l)
print(id(l))  # After multiplication, the list is the same object, with new items appended
t = (1, 2, 3)
print(type(t))
print(id(t))  # ID of the initial tuple
t *= 2
print(id(t))  # After multiplication, a new tuple was created

# 让我们再看看immutable
# An intriguing corner case that highlights what “immutable” really means in the context of tuples.

# A += Assignment Puzzler
print('*' * 20 + ' A += Assignment Puzzler ' + '*' * 20)
t = (1, 2, [30, 40])
# t[2] += [50, 60] # 这句话编译通不过哦,解释如下:
# console test
# In [27]: t = (1, 2, [30, 40])
#
# In [28]: t[2] += [50, 60]
# ---------------------------------------------------------------------------
# ImportError                               Traceback (most recent call last)
# /Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/flask_script/commands.py in run(self, no_ipython, no_bpython)
#     299                     # 0.10.x
# --> 300                     from IPython.Shell import IPShellEmbed
#     301                     ipshell = IPShellEmbed(banner=self.banner)
#
# ImportError: No module named 'IPython.Shell'
#
# During handling of the above exception, another exception occurred:
#
# TypeError                                 Traceback (most recent call last)
# <ipython-input-28-9f190ddb433c> in <module>()
# ----> 1 t[2] += [50, 60]
#
# TypeError: 'tuple' object does not support item assignment
#
# In [29]: t
# Out[29]: (1, 2, [30, 40, 50, 60])

### t居然变化了! ###
# 发生了什么呢?
# 1. 去看看http://www.pythontutor.com/
# 2. console:
from dis import dis

dis('s[a] += b')
# 1           0 LOAD_NAME                0 (s)
#             3 LOAD_NAME                1 (a)
#             6 DUP_TOP_TWO
#             7 BINARY_SUBSCR
#             8 LOAD_NAME                2 (b)
#            11 INPLACE_ADD
#            12 ROT_THREE
#            13 STORE_SUBSCR
#            14 LOAD_CONST               0 (None)
#            17 RETURN_VALUE

# 分析如下:
# 7  Put the value of s[a] on TOS (Top Of Stack).
# 11 Perform TOS += b. This succeeds if TOS refers to a mutable object (it’s a list)
# 13 Assign s[a] = TOS. This fails if s is immutable (the t tuple)

# This example is quite a corner case — in 15 years of using Python, I have never seen this strange behavior actually bite somebody.
# I take three lessons from this:
# 1. Putting mutable items in tuples is not a good idea.
# 2. Augmented assignment is not an atomic operation — we just saw it throwing an exception after doing part of its job.
# 3. Inspecting Python bytecode is not too difficult, and is often helpful to see what is going on under the hood.
