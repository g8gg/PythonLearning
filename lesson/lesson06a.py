# Object and Class
# lesson 06 a
# Hidden/Private Attribute, Protected Property, Instance Method

class Duck:
    def __init__(self, input_name):
        self.hidden_name = input_name

    def get_name(self):
        print('inside the getter')
        return self.hidden_name

    def set_name(self, input_name):
        print('insde the setter')
        self.hidden_name = input_name

    def del_name(self):
        del self.hidden_name

    name = property(get_name, set_name, del_name, "I'm the 'name' property")


class DuckNew:
    def __init__(self, input_name):
        self.hidden_name = input_name

    @property
    def name(self):
        print('inside the getter')
        return self.hidden_name

    @name.setter
    def name(self, input_name):
        print('insde the setter')
        self.hidden_name = input_name


fowl = Duck('Howard')
print(fowl.name)
print(fowl.get_name())  # call method
fowl.name = 'Davie'
fowl.set_name('Dave')

print('-' * 80)
fowl = DuckNew('Mike')  # no getter & setter
print(fowl.name)
fowl.name = 'Micheal'
print(fowl.name)


# private property
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    # 计算属性, 使用Property可以设定属性只读;
    # 可以计算属性, 根据属性变化自动更新值;
    # 如果改了某个特性的值, 只需要修改定义(类内修改,其他使用属性的地方不变化)
    def diameter(self):  # 无setter, 只读
        return 2 * self.radius


print('Circle', '-' * 80)
c = Circle(5)
print(c.radius, c.diameter)
c.radius = 7
print(c.radius, c.diameter)  # 计算属性自动更新


# c.diameter = 18  # AttributeError: can't set attribute


# protected private property
class X:
    def __init__(self, x):
        print("init")
        self.__x = x  # Python的命名规范, 约定连续两个下划线开头的,就是隐藏在内部的特性(attribute)

    @property
    def x(self):
        print('inside the getter')
        return self.__x

    @x.setter
    def x(self, x):
        print('inside the setter')
        self.__x = x


print('Hacking', '-' * 80)
anonymous = X('')  # init
anonymous.x = '6bi47X'  # setter
print(anonymous.x)  # getter     Python本质上并没有把特性变成私有,但是确实把名字重整,让外部代码无法使用
# Hacking that now ! 绕过了getter和setter哦
# no setter and getter
print('no setter & no getter')
anonymous._X__x = 'heiheihei'
print(anonymous._X__x)  # 用这种方式, 可以直接访问到私有变量(其实就是改了名字,做了保护,哈哈哈,不过至少避免了你直接使用或改变)
# getter
print(anonymous.x)
# 这也说明Python的特性完全公开设计是真实的, 并没有黑科技
