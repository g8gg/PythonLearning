# Slicing
# 我们都知道sequences can be sliced using the s[a:b] syntax
# 所有的sequence types都支持切片,如: list, tuple, str

# Why Slices and Range Exclude the Last Item
# The Pythonic convention of excluding the last item in slices and ranges works well with the zero-based indexing
#  used in Python, C, and many other languages. Some convenient features of the convention are:
# 1. It’s easy to see the length of a slice or range when only the stop position is given: range(3) and my_list[:3] both produce three items.
# 2. It’s easy to compute the length of a slice or range when start and stop are given: just subtract stop - start.
# 3. It’s easy to split a sequence in two parts at any index x, without overlapping: simply get my_list[:x] and my_list[x:]. For example:
l = [10, 20, 30, 40, 50, 60]
print(l[:2])  # split at 2
print(l[2:])
print(l[:3])  # split at 3
print(l[3:])

# Slice Objects
# This is no secret, but worth repeating just in case: s[a:b:c] can be used to specify a stride or step c, causing the
# resulting slice to skip items. The stride can also be negative, returning items in reverse.
# Three examples make this clear:
s = 'bicycle'
print(s[::3])
print(s[::-1])
print(s[::-2])


# The notation a:b:c is only valid within [] when used as the indexing or subscript operator,
# and it produces a slice object: slice(a, b, c).

# How Slicing Works ?
# Checking out the behavior of __getitem__ and slices
class MySeq:
    def __getitem__(self, index):
        return index  # For this demonstration, __getitem__ merely returns whatever is passed to it.


s = MySeq()
print(s[1])  # A single index, nothing new.
print(s[1:4])  # The notation 1:4 becomes slice(1, 4, None).
print(s[1:4:2])  # slice(1, 4, 2) means start at 1, stop at 4, step by 2.
print(s[1:4:2, 9])  # Surprise: the presence of commas inside the [] means __getitem__ receives a tuple.
print(s[1:4:2, 7:9])  # The tuple may even hold several slice objects.

invoice = """
    0.....6.................................40........52...55........
    1909  Pimoroni PiBrella                     $17.50    3    $52.50
    1489  6mm Tactile Switch x20                 $4.95    2     $9.90
    1510  Panavise Jr. - PV-201                 $28.00    1    $28.00
    1601  PiTFT Mini Kit 320x240                $34.95    1    $34.95
    """
SKU = slice(0, 6)
DESCRIPTION = slice(6, 40)
UNIT_PRICE = slice(40, 52)
QUANTITY = slice(52, 55)
ITEM_TOTAL = slice(55, None)
line_items = invoice.split('\n')[2:]
for item in line_items:
    print(item[UNIT_PRICE], item[DESCRIPTION])

### Inspecting the attributes of the slice class
print(slice)  # slice is a built-in type
print(dir(slice))  # Inspecting a slice we find the data attributes start, stop, and step, and an indices method.
help(slice.indices)

# Multidimensional Slicing and Ellipsis
# The [] operator can also take multiple indexes or slices separated by commas. This is used, for instance, in the
# external NumPy package, where items of a two-dimensional numpy.ndarray can be fetched using the syntax a[i, j] and a
# two-dimensional slice obtained with an expression like a[m:n, k:l].
# 参见原书讨论

# Assigning to Slices
l = list(range(10))
print(l)
l[2:5] = [20, 30]
print(l)
del (l[5:7])
print(l)
l[3::2] = [11, 22]
print(l)
# l[2:5] = 100 #  When the target of the assignment is a slice, the right side must be an iterable object, even if it has just one item.
# TypeError: can only assign an iterable
#     S.indices(len) -> (start, stop, stride)
l[2:5] = [100]
print(l)
print(l[2:2])
print(l[2:3])