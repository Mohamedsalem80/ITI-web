# 1. Rainbow colors list
rainbow_colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

# a) Print out the fourth item
print("1.a Fourth item:", rainbow_colors[3])

# b) Slice from 3rd to end into new list
colors = rainbow_colors[2:]
print("1.b Sliced list (colors):", colors)

# c) Range of items from 2nd to 5th
print("1.c 2nd–5th items:", rainbow_colors[1:5])

# d) Update fourth item to white
rainbow_colors[3] = "white"
print("1.d Updated 4th item:", rainbow_colors[3])
print("    Updated rainbow_colors:", rainbow_colors)

# e) Change violet → brown
for i, c in enumerate(rainbow_colors):
    if c == "violet":
        rainbow_colors[i] = "brown"
        break
print("1.e violet → brown:", rainbow_colors)


# 2. Work with numbers and extending rainbow_colors
numbers = [1, 3.7, 6, 8]

# a) Add gray
rainbow_colors.append("gray")
print("2.a Added gray:", rainbow_colors)

# b) Add pink as first element
rainbow_colors.insert(0, "pink")
print("2.b Added pink at first:", rainbow_colors)

# c) Add numbers list to rainbow_colors
rainbow_colors.extend(numbers)
print("2.c After adding numbers list:", rainbow_colors)

# d) Remove 6 from numbers
numbers.remove(6)
print("2.d numbers after removing 6:", numbers)

# e) Remove all rainbow_colors
rainbow_colors.clear()
print("2.e rainbow_colors cleared:", rainbow_colors)


# 3. Countries list
countries = ["UK", "Egypt", "UAE", "France", "Oman", "France", "USA", "Italy", "UAE", "Egypt"]

# a) Remove last
countries.pop()
print("3.a Remove last:", countries)

# b) Remove first
countries.pop(0)
print("3.b Remove first:", countries)

# c) Index of France
print("3.c Index of 'France':", countries.index("France"))

# d) Count Egypt
print("3.d Count of 'Egypt':", countries.count("Egypt"))

# e) Sort by length
countries.sort(key=len)
print("3.e Sorted by length:", countries)

# f) Reverse into new list
rev_list = list(reversed(countries))
print("3.f rev_list:", rev_list)

# g) Reverse in place
countries.reverse()
print("3.g countries reversed in place:", countries)


# 4. Numbers 1–9
int_list = list(range(1, 10))

# a) Sort descending
int_list.sort(reverse=True)
print("4.a Descending:", int_list)

# b) Sort ascending
int_list.sort()
print("4.b Ascending:", int_list)

# c) Clone into new_list
new_list = int_list.copy()
print("4.c new_list cloned:", new_list)

# d) Remove range 2–8
# keep only <2 or >8
new_list = [n for n in new_list if n < 2 or n > 8]
print("4.d new_list after removing 2–8:", new_list)
