# https://docs.python.org/3/library/configparser.html
import configparser

config = configparser.ConfigParser()
config.read('example.ini')
print(config.sections())
print('gosber.org' in config)
print(config['gosber.org']['User'])
print(config['DEFAULT']['Compression'])
g8gg = config['g8gg.server.com']
print(g8gg['ForwardX11'])
print(g8gg['Port'])

for key in config['gosber.org']: print(key)

print(config['gosber.org']['ForwardX11'])

# Supported Datatypes
print(float(g8gg['CompressionLevel']))
print(g8gg.getboolean('ForwardX11'))

# Fallback Values
print(g8gg.get('CompressionLevel', 3.1))
print(g8gg.get('CompressionLevel1', 3.1))

# Supported INI File Structure
# A configuration file consists of sections, each led by a [section] header,
# followed by key/value entries separated by a specific string (= or : by default [1]).
# By default, section names are case sensitive but keys are not [1].
# Leading and trailing whitespace is removed from keys and values. Values can be omitted,
# in which case the key/value delimiter may also be left out. Values can also span multiple lines,
# as long as they are indented deeper than the first line of the value.
# Depending on the parser’s mode, blank lines may be treated as parts of multiline values or ignored.
#
# Configuration files may include comments, prefixed by specific characters (# and ; by default [1]).
#  Comments may appear on their own on an otherwise empty line, possibly indented.

# For example:
# [Simple Values]
# key=value
# spaces in keys=allowed
# spaces in values=allowed as well
# spaces around the delimiter = obviously
# you can also use : to delimit keys from values
#
# [All Values Are Strings]
# values like this: 1000000
# or this: 3.14159265359
# are they treated as numbers? : no
# integers, floats and booleans are held as: strings
# can use the API to get converted values directly: true
#
# [Multiline Values]
# chorus: I'm a lumberjack, and I'm okay
#     I sleep all night and I work all day
#
# [No Values]
# key_without_value
# empty string value here =
#
# [You can use comments]
# # like this
# ; or this
#
# # By default only in an empty line.
# # Inline comments can be harmful because they prevent users
# # from using the delimiting characters as parts of values.
# # That being said, this can be customized.
#
#     [Sections Can Be Indented]
#         can_values_be_as_well = True
#         does_that_mean_anything_special = False
#         purpose = formatting for readability
#         multiline_values = are
#             handled just fine as
#             long as they are indented
#             deeper than the first line
#             of a value
#         # Did I mention we can indent comments, too?


#  Interpolation of values¶
# [Paths]
# home_dir: /Users
# my_dir: %(home_dir)s/lumberjack
# my_pictures: %(my_dir)s/Pictures
# # class configparser.BasicInterpolation
