# 1. Loop through colors and skip "blue"
colors = ["red", "blue", "yellow", "orange", "green"]

print("1. Colors (skip blue):")
for c in colors:
    if c == "blue":
        continue
    print(c)

# 2. Valid vs invalid tuple/list assignments
print("\n2. Tuple/List assignment tests:")

# a) valid (list inside list)
a = [1, 2, 3, 4, [7, 8, 9]]
a[4][1] = 300
print("  a) ", a)

# b) invalid (tuple inside list → tuple is immutable)
print("  b)  (This will raise a TypeError if uncommented)")
# a = [1, 2, 3, 4, (7, 8, 9)]
# a[4][1] = 300  # ❌ TypeError: 'tuple' object does not support item assignment
# print(a)

# c) valid (tuple containing a list; list is mutable)
a = (1, 2, 3, 4, [7, 8, 9])
a[4][1] = 300
print("  c) ", a)

# 3. Pattern printing
print("\n3. Pattern:")
for i in range(1, 4):
    print("#" * i)
for i in range(2, 0, -1):
    print("#" * i)

# 4. Factorial of a number
print("\n4. Factorial calculator:")
num = int(input("Enter a number: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print("Factorial of", num, "is", fact)
