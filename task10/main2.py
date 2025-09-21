# 1. Create the tuple
sub = ("C++", "java", "python", 50, True, 36.2)

# a) Print 2nd item
print("1.a Second item:", sub[1])

# b) Slice 1st→3rd (index 0..2)
sub_mini = sub[0:3]
print("1.b sub_mini:", sub_mini)

# c) 2nd→last
print("1.c 2nd to last:", sub[1:])

# d) Tuples are immutable → make a new one with last changed
sub = sub[:-1] + (85.6,)
print("1.d Updated last item:", sub[-1])
print("    Updated sub tuple:", sub)

# e) Unpack
x1, x2, x3, x4, x5, x6 = sub
print("1.e Unpacked:", x1, x2, x3, x4, x5, x6)

# f) Concatenate
sub_add = sub + sub_mini
print("1.f sub_add:", sub_add)

# g) Index of "python"
print("1.g Index of python:", sub_add.index("python"))

# h) Count of 36.2
print("1.h Count of 36.2:", sub_add.count(36.2))

# i) Length
print("1.i Length of sub_add:", len(sub_add))

# j) Convert to list
sub_list = list(sub_add)
print("1.j sub_add as list:", sub_list)

# k) Delete the tuple
del sub
print("1.k sub deleted (can't print it now)")

# ------------------------------------------------------------------
# 2. Convert string to list of words
sentence = "Welcome to the university"
words_list = sentence.split()
print("2. Words list:", words_list)

# 3. Tuple to string
letters = ("p", "y", "t", "h", "o", "n")
joined_string = "".join(letters)
print("3. Joined string:", joined_string)

# ------------------------------------------------------------------
# 4. Outputs of small tuple/list programs
# a)
a_tuple = (4, 77, 3, [98, 15])
a_tuple[3][0] = 44
print("4.a", a_tuple)          # tuple itself immutable but list inside mutable

# b)
b_tuple = ("python")
print("4.b", type(b_tuple))    # plain string, not tuple

# c)
c_tuple = ("python",)
print("4.c", type(c_tuple))    # tuple with one element

# d)
d_tuple = "java",
print("4.d", type(d_tuple))    # trailing comma makes tuple

# e)
e_wor = "Data"
print("4.e", list(e_wor))      # ['D','a','t','a']

# f)
f_wor = "info"
print("4.f", tuple(f_wor))     # ('i','n','f','o')

# g)
g_tuple = ("a", "b", "c", "d")
print("4.g", list(g_tuple))

# h)
print("4.h", list())

# i)
print("4.i", tuple())

# j)
print("4.j", ("why","??") * 4)

# k)
print("4.k", ["hi!",] * 3)

# l) (looks like 1 instead of l)  prints same as k
print("4.l", ["hi!"] * 3)

# m)
sub_str = "python, c++, java"
print("4.m", sub_str.split(","))
