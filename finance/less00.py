from math import *
from datetime import *

loops = 250000
a = range(1, loops)


def f(x):
    return 3 * log(x) + cos(x) ** 2


r = [f(x) for x in a]
print(r)
