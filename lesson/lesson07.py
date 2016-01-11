# Data
# Unicode is good
# Lesson 07
import unicodedata as uni

asc = '\u0061' + '\u0041'  # unicode, plane 00:xx is ASCII table
print(asc)


def unicode_test(value):
    name = uni.name(value)
    value2 = uni.lookup(name)
    print('value="%s",name="%s",value2="%s"' % (value, name, value2))


unicode_test('A')
unicode_test('\u00a2')
unicode_test('\u20ac')
unicode_test('\u2603')
unicode_test('\u9a6c')

# 测试\N 用名称查找字符
char_name = uni.name('\u00e9')
print(char_name)
print(uni.lookup(char_name))  # 注意Python和Unicode字符名称索引页的字符名称可能不一致
place = 'caf\N{LATIN SMALL LETTER E WITH ACUTE}'
print(place)

# encode & decode
# encode
snowman = '\u2603'
ds = snowman.encode('utf-8')
print(len(ds), ds)

# utf8的字符超越了ascii,所以没法转换了,所以会出错
try:
    snowman.encode('ascii')
except Exception as err:
    print(err)
    print(snowman.encode('ascii', 'ignore'))  # 忽略
    print(snowman.encode('ascii', 'replace'))  # 替换
    print(snowman.encode('ascii', 'backslashreplace'))  # unicode-escape 可打印版本
    print(snowman.encode('ascii', 'xmlcharrefreplace'))  # 网页中使用的字符实体串

print('-' * 80)
# decode
# 将字节串转化为unicode字符串
# 问题在于,字节串!并不自带编码方式的信息
place = 'café'
print(type(place))
place_bytes = place.encode('utf-8')
print(place_bytes)
print(type(place_bytes))
place2 = place_bytes.decode('utf-8')
print(place2)

try:
    place_bytes.decode('ascii')
except Exception as err:
    print(err)
    print(place_bytes.decode('ascii', 'ignore'))  # 忽略
    print(place_bytes.decode('ascii', 'replace'))  # 替换

print(place_bytes.decode('latin-1'))
print(place_bytes.decode('windows-1252'))

# format
try:
    print("Test missing one %s, %s" % ('test'))
    # TypeError: not enough arguments for format string
except Exception as err:
    print(err)
