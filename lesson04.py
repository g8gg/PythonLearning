# Lesson 04
# namespace and scope
# exception handle

str_global = 'global'


def change_global():
    """ try scope """
    # local variable 'str_global' referenced before assignment
    # print(str_global)  # 你不能使用或者改变outer scope的变量
    str_global = 'g'  # shadows name from outer scope


change_global()


def change_local():
    str_global = 'local'
    print(str_global, id(str_global))


print(str_global, id(str_global))
change_local()


# 使用全局变量
def change_global_right():
    global str_global
    str_global = "修改global"
    print(__name__, globals())
    print('*' * 80)
    print(__name__, locals())


change_global_right()
print("global changed:", str_global, id(str_global))  # 值变了,但是id也变了


def get_value():
    short_list = [x for x in range(0, 10)]
    position = 0
    while True:
        value = input('Position [q to quit]?')
        if value == 'q':
            break
        try:
            position = int(value)
            print(short_list[position])
        except IndexError as error:
            print('Bad index:', position, 'Err:', error)
        except Exception as otherErr:
            print('Something else broke:', otherErr)


get_value()  # try to catch exception


# customize exception
# a exception is a class, it's a subclass of Exception class
class UppercaseException(Exception):
    pass


words = ['test', 'MO', 'some', 'TO']
for word in words:
    try:
        if word.isupper():
            raise UppercaseException(word)
    except UppercaseException as err:
        print('Upper word found →', err)
    except Exception as other:
        print('Something else broke:', other)
