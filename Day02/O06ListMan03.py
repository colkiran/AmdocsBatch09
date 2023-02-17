
print("remove".center(40, "-"))

l1 = [1, 2, 1, 1, 1, 2, 3, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 3, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 3, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2]
print(f"l1 :{l1}")

print("-" * 40)
l1.remove(3)
l1.remove(3)
l1.remove(3)

print(f"l1 :{l1}")

# remove all 1's from the list
while l1.count(1):
    l1.remove(1)

print(f"l1 : {l1}")

print("index".center(40, "-"))

l1 = [1, 2, 1, 1, 1, 2, 3, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 3, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 3, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2]
print(f"l1 :{l1}")

print(l1.index(3))
print(l1.index(3, l1.index(3)+1))
print(l1.index(3, l1.index(3, l1.index(3)+1)+1))

print("revere".center(40,"-"))
l1 = [10, 5, 7, 1, 9, 3, 6, 2, 8, 4]
print(f"l1 :{l1}")

# reverse - change the original list
# reversed - returns a copy of the reversed list

res = list(reversed(l1))
print(f"res: {res}")

l1.reverse()
print(f"l1 :{l1}")
