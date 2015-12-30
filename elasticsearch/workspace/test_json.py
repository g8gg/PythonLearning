from json import encoder, decoder, dump, dumps, load, loads, JSONEncoder
from io import StringIO
from decimal import Decimal

# Encoding basic Python object hierarchies:
print(dumps(['foo', {'bar': ('baz', None, 1.0, 2)}]))
print(dumps("\"foo\bar"))
print(dumps('\u1234'))
print(dumps('\\'))
print(dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True))

io = StringIO()
dump(['streaming API'], io)
io.getvalue()

# Compact encoding:
print(dumps([1, 2, 3, {'4': 5, '6': 7}], separators=(',', ':')))

# Pretty printing:
print(dumps({'4': 5, '6': 7}, sort_keys=True, indent=4))

# Decoding JSON:
print(loads('["foo", {"bar":["baz", null, 1.0, 2]}]'))
print(loads('"\\"foo\\bar"'))
io = StringIO('["streaming API"]')
print(load(io))


# Specializing JSON object decoding:
def as_complex(dct):
    if '__complex__' in dct:
        return complex(dct['real'], dct['imag'])
    return dct


print(loads('{"__complex__": true, "real": 1, "imag": 2}',
            object_hook=as_complex))
print(loads('1.1', parse_float=Decimal))


# Extending JSONEncoder:
class ComplexEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, complex):
            return [obj.real, obj.imag]
        # Let the base class default method raise the TypeError
        return JSONEncoder.default(self, obj)


print(dumps(2 + 1j, cls=ComplexEncoder))
print(ComplexEncoder().encode(2 + 1j))
print(list(ComplexEncoder().iterencode(2 + 1j)))
