list = []

# APPEND
list.append(1)
list.append("Python")
list.append([10, 20, 30])
print(f"List: {list}")

# COPY - copy list with new id
new_list = list.copy()
print(f"""
      Old list: id[{id(list)}] => {list}
      New list: id[{id(new_list)}] => {new_list}""")

# COUNT
colors = ["red", "green", "green", "black", "white", "white", "white"]
red_color = colors.count("red")
green_color = colors.count("green")
white_color = colors.count("white")

print(f"Red: {red_color}")
print(f"Green: {green_color}")
print(f"White: {white_color}")

# EXTEND
languages = ["python", "c", "c++"]
print(f"Languages: {languages}")

languages.extend(["js", "ruby", "java"])
print(f"Languages: {languages}")

# INDEX
languages = ["python", "c", "c++", "js", "ruby", "java"]
java_index = languages.index("java")
python_index = languages.index("python")
print(f"Java index: [{java_index}]")
print(f"Python index: [{python_index}]")

# POP
languages = ["python", "c", "c++", "js", "ruby", "java"]
print(f"Languages Pop: {languages.pop()}")
print(f"Languages Pop: {languages.pop()}")
print(f"Languages Pop[0]: {languages.pop(0)}")

# REMOVE
languages = ["python", "c", "c++", "js", "ruby", "java"]
languages.remove("c")
print(f"Languages Remove: {languages}")

# REVERSE
languages = ["python", "c", "c++", "js", "ruby", "java"]
languages.reverse()
print(f"Languages Reverse: {languages}")

# SORT / Lambda is a anonym function
languages = ["python", "c", "c++", "js", "ruby", "java"]
languages.sort()
print(f"Languages Sort: {languages}")
languages.sort(reverse=True)
print(f"Languages Sort Reverse: {languages}")
languages.sort(key=lambda x: len(x), reverse=True)
print(f"Languages Sort Key Reverse: {languages}")

# LEN
languages = ["python", "c", "c++", "js", "ruby", "java"]
print(f"Languages Length: {len(languages)}")

# SORTED
languages = ["python", "c", "c++", "js", "ruby", "java"]
print(f"Languages Sorted: {sorted(languages)}")

lee = [n**2 if n > 6 else n for n in range(10) if n % 2 == 0]
print(lee)

new_arr = []
for n in range(10):
    if n % 2 == 0:
        if n > 6:
            new_arr.append(n ** 2)
        else:
            new_arr.append(n)
print(new_arr)
