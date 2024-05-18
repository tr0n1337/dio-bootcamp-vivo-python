course = "PyThOn"

# UPPERCASE
UPPERCASE = course.upper()
print(f"Method upper(): {UPPERCASE}")  # PYTHON

# LOWER
LOWER = course.lower()
print(f"Method lower(): {LOWER}")  # python

# TITLE
TITLE = course.title()
print(f"Method title(): {TITLE}")  # Python

# ========================================

course = "     Python  "

# STRIP
STRIP = course.strip()
print(f"Method strip(): {STRIP}")  # Remove all whitespaces

# LSTRIP
LSTRIP = course.lstrip()
print(f"Method lstrip(): {LSTRIP}")  # Remove left whitespaces

# RSTRIP
RSTRIP = course.rstrip()
print(f"Method rstrip(): {RSTRIP}")  # Remove right whitespaces

# ========================================

course = "Python"

# CENTER
CENTER = course.center(10, "#")
print(f"Method center(): {CENTER}")  # ##Python##

# JOIN
JOIN = ".".join(course)
print(f"Method join(): {JOIN}")  # P.y.t.h.o.n
