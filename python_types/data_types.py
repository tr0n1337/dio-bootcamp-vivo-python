text = "str"
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

print('''
  Text: {text}
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
'''.format(text=text,
           int_number=int_number,
           float_number=float_number,
           complex_number=complex_number,
           tuple_sequence=tuple_sequence,
           list_sequence=list_sequence,
           range_sequence=range_sequence,
           dict_map=dict_map,
           set_collection=set_collection,
           frozenset_collection=frozenset_collection,
           false_bool=false_bool,
           true_bool=true_bool,
           bytes_binary=bytes_binary,
           bytearray_binary=bytearray_binary,
           memory_view_binary=memory_view_binary))
