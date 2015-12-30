from config.named_constants import Constants


class MyConstants(Constants):
    PI = 3.141592653589793
    E = 2.718281828459045
    AUTHOR = "周小雪"


class Colors(Constants):
    red, yellow, green, blue, white = range(5)


class FigConstants(Constants):
    @classmethod
    def read(cls, i):
        return cls(int(i))

    def other(self):
        return "test method"


class ObjectType(FigConstants):
    CustomColor = 0
    Ellipse = 1
    Polygon = 2
    Spline = 3
    Text = 4
    Arc = 5
    CompoundBegin = 6
    CompoundEnd = -6


import doctest


def test_README():
    failure_count, test_count = doctest.testfile('README.rst', verbose=True)
    assert test_count > 0
    assert failure_count == 0


def test_Colors():
    assert Colors.green == 2


def test_ObjectType():
    assert in ObjectType
    assert 'other' not in ObjectType


n = 2
m = 3
a = {n, m}
print(a)

MyConstants.pi = 3.14
print(MyConstants.PI)

test_Colors()
test_ObjectType()
# test_README()
