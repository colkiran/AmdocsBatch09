
l1 = list()
print(f"l1 :{l1}")
print(type(l1))

print("-" * 40)
l2 = [1, 2, 3, 'four', 'five', 'six', 7.8, 8.3, 9.0, 10+2j, 10-2j, True, False]
print(f"l2 :{l2}")

# memory allocation
print(id(l2[0]))
print(id(l2[1]))
print(id(l2[2]))
print(id(l2[3]))
print(id(l2[4]))

print("-" * 40)
l3 = list(range(1, 11))
print(f"l3 :{l3}")
print(type(l3))

print("-" * 40)
l1 = list(range(1, 6))
print(f"l1 :{l1}")

# read
print(f"l1[0] :{l1[0]}")
print(f"l1[3] :{l1[3]}")

# iterate
for i in l1:
    print(i, end=" ")
print()

# modify
l1[2] = 33          # insert
l1[4] = 55
# l1[5] = 6
print(f"l1 :{l1}")

# delete
print(f"l1 :{l1}")
del l1[2]
del l1[3]

print(f"l1 :{l1}")

print("-" * 40)
print(dir(l1))