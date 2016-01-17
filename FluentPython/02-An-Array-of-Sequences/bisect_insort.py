# Like bisect, insort takes optional lo, hi arguments to limit the search to a sub-sequence.
# There is also an insort_left variation that uses bisect_left to find insertion points.
import bisect
import random

SIZE = 7

random.seed(1729)

my_list = []
for i in range(SIZE):
    new_item = random.randrange(SIZE * 2)
    bisect.insort(my_list, new_item)  # Insert x in a in sorted order.
    #  This is equivalent to a.insert(bisect.bisect_left(a, x, lo, hi), x) assuming that
    # a is already sorted. Keep in mind that the O(log n) search is dominated by the slow O(n) insertion step.
    print('%2d ->' % new_item, my_list)
