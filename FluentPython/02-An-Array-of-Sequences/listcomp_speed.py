# 重点:
# List/Tuple
import timeit

TIMES = 10000

SETUP = """
symbols = '$¢£¥€¤'
def non_ascii(c):
    return c > 127
"""


def clock(label, cmd):
    res = timeit.repeat(cmd, setup=SETUP, number=TIMES)
    print(label, *('{:.3f}'.format(x) for x in res))


# a simple speed test comparing listcomp with filter/map.
# 比较一下,看看listcomp快还是filter/map更快
clock('listcomp        :', '[ord(s) for s in symbols if ord(s) > 127]')
clock('listcomp + func :', '[ord(s) for s in symbols if non_ascii(ord(s))]')
clock('filter + lambda :', 'list(filter(lambda c: c > 127, map(ord, symbols)))')
clock('filter + func   :', 'list(filter(non_ascii, map(ord, symbols)))')

if __name__ == '__main__':
    # 请仔细体会:listcomps and genexps!
    # For brevity, many Python programmers refer to list comprehensions as listcomps,
    #  and generator expressions as genexps. I will use these words as well.

    # Build a list of Unicode codepoints from a string
    symbols = '$¢£¥€¤'
    codes = []
    # A for loop may be used to do lots of different things: scanning a sequence to count or pick items, computing
    #  aggregates (sums, averages), or any number of other processing tasks.
    for symbol in symbols:
        codes.append(ord(symbol))
    print(codes)

    # Take 2,more readable because its intent is explicit.
    # The code is building up a list. In contrast, a listcomp is meant to do one thing only: to build a new list.
    codes = [ord(symbol) for symbol in symbols]
    print(codes)

    # BUT,不要滥用该原则,因为
    # Of course, it is possible to abuse list comprehensions to write truly incomprehensible code. I’ve seen Python code
    #  with listcomps used just to repeat a block of code for its side effects. If you are not doing something with the
    # produced list, you should not use that syntax. Also, try to keep it short. If the list comprehension spans
    # more than two lines, it is probably best to break it apart or rewrite as a plain old for loop.
    # Use your best judgment: for Python as for English, there are no hard-and-fast rules for clear writing.

    # 语法技巧
    # In Python code, line breaks are ignored inside pairs of [], {}, or (). So you can build multiline lists,
    # listcomps, genexps, dictionaries and the like without using the ugly \ line continuation escape.


    # Listcomps Versus map and filter
    # The same list built by a listcomp and a map/filter composition
    print('*' * 10 + " Listcomps Versus map and filter " + '*' * 10)
    beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
    print(beyond_ascii)
    beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))  # map and filter, λ表达式
    print(beyond_ascii)

    # Cartesian product using a list comprehension
    print('*' * 10 + " Cartesian product using a list comprehension " + '*' * 10)
    colors = ['black', 'white']
    sizes = ['S', 'M', 'L']
    # Take 1
    # here the six-item list of T-shirts is never built in memory:
    # the generator expression feeds the for loop producing one item at a time.
    # If the two lists used in the Cartesian product had 1,000 items each,
    #  using a generator expression would save the expense of
    # building a list with a million items just to feed the for loop.
    tshirts = [(color, size) for color in colors for size in
               sizes]  # generate a list of tuples arranged by color, then size
    print(tshirts)
    #
    # Take 2
    for color in colors:
        for size in sizes:
            print((color, size))
    # Take 3 To get items arranged by size, then color, just rearrange the for clauses; adding a line break to the
    # istcomp makes it easy to see how the result will be ordered.
    tshirts = [(color, size) for size in sizes
               for color in colors]

    # 注意:
    # Listcomps are a one-trick pony: they build lists. To fill up other sequence types, a genexp is the way to go.
    print('*' * 20 + " CGenerator Expressions " + '*' * 20)
    ###
    # Generator Expressions
    # look at genexps in the context of building nonlist sequences.
    # To initialize tuples, arrays, and other types of sequences, you could also start from a listcomp, but a genexp
    # saves memory because it yields items one by one using the iterator protocol instead of building a whole list
    # just to feed another constructor.

    # initializing a tuple and an array from a generator expression
    x = tuple(ord(symbol) for symbol in symbols)
    print(x)
    import array

    a = array.array('I', (ord(symbol) for symbol in symbols))
    print(a)

    # uses a genexp with a Cartesian product to print out a roster of T-shirts of two colors in three sizes.
    for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
        print(tshirt)
    # The generator expression yields items one by one;
    # a list with all six T-shirt variations is never produced in this example.

    ### 元组
    print('*' * 20 + " 元组 " + '*' * 20)
    # 元组一般用来作为不可变list,但是TA还可以用作没有字段名的记录
    # Tuples Are Not Just Immutable Lists
    # Some introductory texts about Python present tuples as “immutable lists,” but that is short selling them.
    # Tuples do double duty: they can be used as immutable lists and also as records with no field names.
    # This use is sometimes overlooked, so we will start with that.
    # # Tuples as Records
    # Tuples hold records: each item in the tuple holds the data for one field and the position of the item gives its meaning.
    # If you think of a tuple just as an immutable list, the quantity and the order of the items may
    # or may not be important, depending on the context. But when using a tuple as a collection of fields,
    #  the number of items is often fixed and their order is always vital.

    # tuples being used as records. Note that in every expression, sorting the tuple would destroy the information
    #  because the meaning of each data item is given by its position in the tuple.
    lax_coordinates = (33.9425, -118.408056)
    traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
    for passport in sorted(traveler_ids):
        print(
                '%s/%s' % passport)  # The % formatting operator understands tuples and treats each item as a separate field.
    for country, _ in traveler_ids:  # The for loop knows how to retrieve the items of a tuple separately — this is called “unpacking.”
        # Here we are not interested in the second item, so it’s assigned to _, a dummy variable.
        print(country)

    ### Tuple Unpacking
    # Tuple unpacking works with any iterable object. The only requirement is that the iterable yields exactly one item
    #  per variable in the receiving tuple, unless you use a star (*) to capture excess items as explained in Using * to
    #  grab excess items. The term tuple unpacking is widely used by Pythonistas, but iterable unpacking is gaining traction,
    # as in the title of PEP 3132 — Extended Iterable Unpacking.
    # a, b, *rest = range(13)
    # print(a, b, rest)
    # a, *b, c, d, e = range(13)
    # print(a, b, c, d, e)

    latitude, longitude = lax_coordinates  # tuple unpacking
    print(latitude, longitude)
    # An elegant application of tuple unpacking is swapping the values of variables without using a temporary variable:
    a = 1
    b = '10'
    b, a = a, b
    print(a, b)
    # Another example of tuple unpacking is prefixing an argument with a star when calling a function:
    print(divmod(20, 8))
    t = (20, 8)
    print(divmod(*t))
    quotient, remainder = divmod(*t)
    print(quotient, remainder)
    # 总结:
    # The preceding code also shows a further use of tuple unpacking:
    # enabling functions to return multiple values in a way that is convenient to the caller.

    # For example, the os.path.split() function builds a tuple (path, last_part) from a filesystem path:
    import os

    path, filename = os.path.split('/usr/gosber/.ssh/idrsa.pub')
    print(path, filename)

    ### Nested Tuple Unpacking
    # Finally, a powerful feature of tuple unpacking is that it works with nested structures.
    # The tuple to receive an expression to unpack can have nested tuples, like (a, b, (c, d)), and Python will do
    # the right thing if the expression matches the nesting structure.

    # Unpacking nested tuples to access the longitude
    print('*' * 20 + " Nested Tuple Unpacking " + '*' * 20)
    metro_areas = [
        # Each tuple holds a record with four fields, the last of which is a coordinate pair.
        ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
        ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
        ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
        ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
        ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
    ]
    print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
    fmt = '{:15} | {:9.4f} | {:9.4f}'

    for name, cc, pop, (latitude, longitude) in metro_areas:
        # By assigning the last field to a tuple, we unpack the coordinates.
        if longitude <= 0:
            print(fmt.format(name, latitude, longitude))

    ### Named Tuples
    print('*' * 20 + " Named Tuples " + '*' * 20)
    # The collections.namedtuple function is a factory that produces subclasses of tuple enhanced
    # with field names and a class name — which helps debugging.
    from collections import namedtuple

    # Defining and using a named tuple type
    City = namedtuple('City', 'name country population coordinates')
    tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
    # 相对比tuple, named tuple的数据必须是位置参数传入来构造
    # Data must be passed as positional arguments to the constructor
    #  (in contrast, the tuple constructor takes a single iterable)
    print(tokyo.name, tokyo.population, tokyo.coordinates)

    # Named tuple attributes and methods (continued from the previous example)
    print(City._fields)  # _fields is a tuple with the field names of the class.
    LatLong = namedtuple('LatLong', 'lat long')
    delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
    delhi = City._make(delhi_data)  # _make() allow you to instantiate a named tuple from an iterable;
    # City(*delhi_data) would do the same.
    print(delhi._asdict())  # _asdict() returns a collections.OrderedDict built from the named tuple instance.
    # That can be used to produce a nice display of city data.
    for key, value in delhi._asdict().items():
        print(key + ':', value)
