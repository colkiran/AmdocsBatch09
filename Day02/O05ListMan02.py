
# add new elements - append, extend, insert

l1 = list(range(1, 6))
print(f"l1 :{l1}")

l1.append(6)
l1.append(7)
l1.append(8)

print(f"l1 :{l1}")

l1.append([9, 10, 11, 12, 13])
print(f"l1 :{l1}")
print(f"l1[8][1:4] :{l1[8][1:4]}")

print("extend".center(40, "-"))
l2 = list(range(2, 11, 2))
print(f"l2 :{l2}")

l2.extend([12, 14, 16])
l2.extend([18, 20, 22])

print(f"l2 :{l2}")

print("insert".center(40, "-"))
l3 = list(range(1, 6))
print(f"l3 :{l3}")

l3.insert(1, 1.5)
l3.insert(3, 2.5)
l3.insert(5, 3.5)
l3.insert(7, 4.5)

print(f"l3 :{l3}")

# delete values from the list - pop, remove, clear

print("clear".center(40, "-"))
l1 = list(range(1, 11))
print(f"l1 :{l1}")

l1.clear()
print(f"l1 :{l1}")

print("pop".center(40, "-"))
l2 = list(range(10, 101, 10))
print(f"l2 :{l2}")

res = l2.pop(8)
print(f"res :{res}")

res = l2.pop(4)
print(f"res :{res}")

res = l2.pop()
print(f"res :{res}")

print(f"l2 :{l2}")

print("count".center(40, "-"))
l1 = [1, 2, 1, 1, 1, 2, 3, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 3, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 3, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2]
print(f"l1 :{l1}")

print("1 :", l1.count(1))
print("2 :", l1.count(2))
print("3 :", l1.count(3))
print("4 :", l1.count(4))


