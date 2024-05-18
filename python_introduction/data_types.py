str = "str"
int_number = 1
float_number = 1.1
complex_number = 3j
list_sequence = ["a", "b", "c"]
tuple_sequence = ("a", "b", "c")  # Unchangeable
range_sequence = range(10)  # Unchangeable
dict_map = {
  "name": "Thiago"
}
set_collection = {1, 2, 3, 4, 5}  # Changeable
frozenset_collection = frozenset({1, 2, 3, 4, 5})  # Unchangeable
false_bool = False
true_bool = True
bytes_binary = bytes('Python', 'utf-8')
bytearray_binary = bytearray([1, 2])
memory_view_binary = memoryview(bytes_binary)

print(f'''
  String: {str}
  Int Number: {int_number}
  Float Number: {float_number}
  Complex Number: {complex_number}
  List Sequence: {list_sequence}
  Tuple Sequence: {tuple_sequence}
  Range Sequence: {range_sequence}
  Dict Map: {dict_map}
  Set Collection: {set_collection}
  Frozen Set Collection: {frozenset_collection}
  False Boolean: {false_bool}
  True Boolean: {true_bool}
  Bytes Binary: {bytes_binary}
  Bytearray Binary: {bytearray_binary}
  MemoryView Binary: {memory_view_binary}
''')
