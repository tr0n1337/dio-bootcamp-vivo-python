first_name = "Thiago"
last_name = "Fernandes"
dict_name = {
  "first_name": "Thiago",
  "last_name": "Fernandes"
}

# FORMAT
FORMAT_1 = "{} {}".format(first_name, last_name)
FORMAT_2 = "{fn} {ln}".format(fn=first_name, ln=last_name)
FORMAT_3 = "{1} {0}".format(last_name, first_name)
FORMAT_4 = "{first_name} {last_name}".format(**dict_name)
print(f"Format: {FORMAT_1}")
print(f"Format: {FORMAT_2}")
print(f"Format: {FORMAT_3}")
print(f"Format: {FORMAT_4}")

# F-STRING
PI = 3.14159
F_STRING = f"PI value: {PI:.2f}"
print(F_STRING)

# SLICING
name = "Thiago de Souza Fernandes"
print(name[0])
print(name[:7])
print(name[10:])
print(name[10:15])
print(name[10:15:2])
print(name[:])
print(name[::-1])  # Revert string

# MULTIPLE LINES
name = "Thiago"
msg = f"""
Hello my name is {name}.
I am learning python.
"""
print(msg)
