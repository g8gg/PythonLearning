# lesson 00
# function & class
from lesson import module


def double_me(me: int):
    """
    just double me
    @type me: int
    @:rtype: int
    """
    return me * 2

print(double_me(2))


class FooBar(object):
    """My First Python Class"""
    version = 0.1  # class (data) attribute

    def __init__(self, nm='G8GG'):
        self.name = nm
        self.nick = "little " + nm
        print('create a class instance for ', nm)

    def show_name(self):
        """display instance attribute and class name"""
        print(self.name)
        print(self.__class__.__name__)

# class example
fooBar = FooBar()
fooBar.show_name()
fooBar = FooBar(nm='Majun')
fooBar.show_name()

# module example
module.somefunc()
print(module.variable)

# some useful funcs below :
# print(int(fooBar)) just for string convert
# print(len(fooBar)) no length


# 注意细节的变化,name和nick并不是开始就有的类属性
print(dir(FooBar))
print(dir(fooBar))

help(FooBar)  # help(fooBar), the same content

print(str(FooBar))
print(str(fooBar))
print(type(FooBar))
print(type(fooBar))
