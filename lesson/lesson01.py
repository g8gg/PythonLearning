# lesson 01
# learning Tuple, List, Dictionary and Set

x, y, z = 1, 2, 3
print(x, y, z)
x, y, z = z, x, y
print(x, y, z)

# x = (y = y + 1) SyntaxError: invalid syntax

lstLocal = ['ZH-CN', 'ZH-TW', 'EN-US']
lstLocal.append('JP')
lstLocal += ['RU']
lstLocal += 'GR'  # look this

print(lstLocal)  # not sorted
print(sorted(lstLocal))  # print sorted result

print(lstLocal)  # no change
lstLocal.sort()  # resort list
print(lstLocal)  # changed

a = [1, 2, 3]
b = a  # reference not copy value
c = a.copy()  # just copy value
a.append(4)
print(b)
b.append(5)
print(a)
print(c)
c.pop()  # delete last one
c0 = c.pop(0)  # delete first one and return it's value
print('c0', c0)
print(c)  # only keep middle one
c.remove(2)
print('c→', c)
print()

x = ['3', '4', '5', '1']
x.insert(0, '0')
x.insert(1, '1')
x.insert(2, '2')
x.remove('1')  # remove first-met element
print('x→', x)
del x[0]  # delete special element
print('x→', x)

x = [2, 3, 1, 2, 3, 1]
x.remove(1)  # remove first-met element
print('x→', x)

# empty_tuple = ()  # empty tuple
empty_tuple = (1, 2, 3, 4, 5)
# empty_tuple[0] = 10  # TypeError: 'tuple' object does not support item assignment
print(empty_tuple)

a, b, c, d, e = empty_tuple
print(a, b, c, d, e)
f = empty_tuple[-1]
print(f)

print("*" * 80)
# dictionary
lots = [[1, 2], [2, 2], [3, 2]]
print(dict(lots))
lots = [(1, 3), (2, 2), (3, 1)]
print(dict(lots))
lots = ((1, 3), (2, 2), (3, 1))
print(dict(lots))
lots = ([1, 3], [2, 2], [3, 1])
print(dict(lots))
str1 = ['ab', 'cd', 'ef', 'gh']
print(dict(str1))
str1 = ('ab', 'cd', 'ef', 'gh')
print(dict(str1))

dictNames = {'马': '骏', '锅': '巴', '锅巴': 'GG'}
print(dictNames)
passNames = {'李': '田', '周': '小', '马': '洋洋'}
dictNames.update(passNames)  # update(merge and overwrite existed)
print(dictNames)
del dictNames['锅巴']  # delete by KEY
print(dictNames)
print()
print(passNames)
passNames.clear()  # empty dict
print(passNames)
print('锅' in dictNames)  # if exists
print('巴' in dictNames)
# print(dictNames['菜'])  # KeyError: '菜'
print(dictNames.get('菜', '不存在'))

# get/access keys and values
print(dictNames.keys())
print(dictNames.values())
print(dictNames.items())
lstItems = list(dictNames.items())  # store KV into list
print(lstItems)
lstItemsCP = lstItems.copy()  # just copy values

# Set()  无序集合
empty_set = set()
char_set = set('马骏就是锅巴GG锅巴GG马骏')
print(char_set)
set1 = set([1, 2, 3, 4, 4, 3, 2, 1, 0])  # list to set()
print(set1)
set2 = set((5, 6, 7, 8, 9, 9, 8, 7, 6, 5))  # tuple to set()
print(set2)
set3 = set({1: 2, 3: 2, 5: 2})  # dictionary to set(), only using KEY
print(set3)
profiles = {
    '000': {'马骏', '男'},
    '001': {'锅巴GG', '男'},
    '002': {'小小', '女'},
}
for code, person in profiles.items():
    print(person)  # 注意,这是无序集合哦!!!

drinks = {
    '高酒精': {'白酒', '黄酒'},
    '无酒精': {'可乐', '雪碧'},
    '低酒': {'红酒', '桃酒'},
}
other_drinks = {'二锅头', '伊力特', '白酒'}

for alcohol, choice in drinks.items():
    if alcohol == '无酒精':
        print(choice)  # 注意,这是无序集合哦!!!
    elif '高酒精' in alcohol and not ('白酒' in choice):
        print(choice)
    elif '高酒精' in alcohol:
        empty_drinks = choice & other_drinks
        inner_drinks = choice | other_drinks
        sub_drinks = choice - other_drinks
        ox_drinks = choice ^ other_drinks
        print()
        print(empty_drinks)
        print(inner_drinks)
        print(sub_drinks)
        print(ox_drinks)  # 异或

# create complex data structure
marxes = ['Grouchos', 'Chico', 'Harpo']
pythons = ['Chapman', 'Cleese', 'Gilliam', 'Jones', 'Palin']
stooges = ['Moe', 'Curly', 'Larry']

tuple_of_lists = marxes, pythons, stooges
print(tuple_of_lists)

list_of_lists = [marxes, pythons, stooges]
print(list_of_lists)

# dict's KEY must be unmutable, so only Tuple can be, List, Dict and Set can't be
dict_of_lists = {'Marxes': marxes, 'Pythons': pythons, 'Stooges': stooges}
print(dict_of_lists)
