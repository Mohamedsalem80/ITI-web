# 1. welcome() function
def welcome(name=None):
    if name is None:
        print("Welcome IT students")
    else:
        print(f"Welcome {name}")

# Demonstration:
welcome()           # prints Welcome IT students
welcome("Mohamed")  # prints Welcome Mohamed

# 2. min_number() to find smallest of three
def min_number(a, b, c):
    return min(a, b, c)

print("\n2. Smallest of (8, 3, 5):", min_number(8, 3, 5))

# 3. abs_value() to return absolute value
def abs_value(n):
    return abs(n)

print("3. Absolute value of -7:", abs_value(-7))

# 4. Solve f(x) = x³ - 4 when x = 4
def f(x):
    return x**3 - 4

result = f(4)
print("4. f(4) =", result)

# 5. Find outputs of given programs
print("\n5.a Program output:")
def f_demo():
    x = "C++"
    print(x)

x = "Python"
f_demo()
print(x)

print("\n5.b Program output:")
def ini_ch(ch1, ch2):
    # Check if first letters match ignoring case
    if ch1[0].lower() == ch2[0].lower():
        return True
    else:
        return False

x = ini_ch("python", "Program")
y = ini_ch("python", "java")
print(x)
print(y)
