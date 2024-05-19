# COUNT
colors = ("red", "red", "green", "white", "white", "white")

red_count = colors.count("red")
green_count = colors.count("green")
white_count = colors.count("white")

print(f"Red Count: {red_count}")
print(f"Green Count: {green_count}")
print(f"White Count: {white_count}")

# INDEX
languages = ("js", "python", "java")

js_index = languages.index("js")
java_index = languages.index("java")

print(f"JS: {js_index}")
print(f"JAVA: {java_index}")

print(isinstance(languages, tuple))
