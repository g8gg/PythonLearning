# try import other module
# 选择自己的风格去使用,只要保持模块的引用和使用是明晰的

import g8ggquote as gq  # import user module from the same path

saying = gq.get_quote()
print('G8GG said:', saying, "", sep='"')


def my_func():
    from g8ggquote import fake as my_fake  # 导入模块的某一部分,并使用别名
    # fake()
    my_fake()


def my_func1():
    from g8ggquote import get_quote  # 导入模块的某一部分
    print(get_quote())


def my_func_global_get():
    from g8ggquote_global import get_author
    print(get_author())


def my_func_global_set(value):
    from g8ggquote_global import set_author
    print(set_author(value))


my_func()
my_func1()
my_func_global_get()
my_func_global_set('小小')
my_func_global_get()  # global variable changed!!!


def print_sys_path():
    import sys
    for place in sys.path:
        print(place)


print_sys_path()
