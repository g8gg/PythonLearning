from math import hypot


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __bool__(self):
        return bool(self.x or self.y)
        # By default, instances of user-defined classes are considered truthy, unless either __bool__ or __len__ is implemented.
        #  Basically, bool(x) calls x.__bool__() and uses the result.
        # If __bool__ is not implemented, Python tries to invoke x.__len__(),
        # and if that returns zero, bool returns False. Otherwise bool returns True.


if __name__ == '__main__':
    v1 = Vector(2, 4)
    v2 = Vector(2, 1)
    print(v1 + v2)
    v = Vector(3, 4)
    print(abs(v))
    print(v * 3)
    print(abs(v * 3))
    print(bool(v1))

    # Summary
    # A basic requirement for a Python object is to provide usable string representations of itself,
    #  one used for debugging and logging, another for presentation to end users.
    # That is why the special methods __repr__ and __str__ exist in the data model.
