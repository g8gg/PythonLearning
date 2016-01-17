# Managing Ordered Sequences with bisect

# BEGIN BISECT_DEMO
import bisect
import sys

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

ROW_FMT = '{0:2d} @ {1:2d}    {2}{0:<2d}'


def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)  # <1> Use the chosen bisect function to get the insertion point.
        offset = position * '  |'  # <2> Build a pattern of vertical bars proportional to the offset.
        print(ROW_FMT.format(needle, position, offset))  # <3> Print formatted row showing needle and insertion point.


if __name__ == '__main__':

    if sys.argv[-1] == 'left':  # <4> Choose the bisect function to use according to the last command-line argument.
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect

    print('DEMO:', bisect_fn.__name__)  # <5> Print header with name of function selected.
    print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
    demo(bisect_fn)

# bisect的行为可以在两个方面微调
# The behavior of bisect can be fine-tuned in two ways.
# 首先,有一对可选参数,lo和hi,允许收缩搜索的范围,默认lo=0,hi=len()
# First, a pair of optional arguments, lo and hi, allow narrowing the region in the sequence to be searched when inserting.
#  lo defaults to 0 and hi to the len() of the sequence.
# 第二,默认bisect的行为是bisect_right,也就是插入点的后面,而如果使用bisect_left,则在之前插入
# Second, bisect is actually an alias for bisect_right, and there is a sister function called bisect_left.
# END BISECT_DEMO
