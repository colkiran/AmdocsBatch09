
print("copy".center(40, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 before :{l1}")

l2 = l1         # shallow copy - it copies the data with the address

print(f"l2 before :{l2}")
l2.extend([6, 7, 8, 9])

print("-" * 40)
print(f"l2 after :{l2}")
print(f"l1 after :{l1}")

print("\n", "-"  * 40,  "\n")

l3 = [2, 4, 6, 8, 10]
print(f"l3 before :{l3}")

l4 = l3.copy()          # deep copy - copies the data to another address

print(f"l4 before :{l4}")
l4.extend([12, 14, 16, 18])

print("-" * 40)
print(f"l4 after :{l4}")
print(f"l3 after :{l3}")

print("\n", "-"  * 40,  "\n")

l5 = [1, 2, 3, [10, 20, 30, 40, 50], 4, 5]      # two dimensional array
print(f"l5 before :{l5}")

l6 = l5.copy()

print(f"l6 before :{l6}")

l6[3].extend([60, 70, 80])
print(f"l6 after :{l6}")
print(f"l5 after :{l5}")

print("\n", "-"  * 40,  "\n")

l7 = [11, 22, 33, 44, [1, 2, 3, 4, 5], 55]
print(f"l7 before :{l7}")
from copy import deepcopy

l8 = deepcopy(l7)

print(f"l8 before :{l8}")

l8[4].extend([6, 7, 8])
print("-" * 40)

print(f"l8 after :{l8}")
print(f"l7 after :{l7}")

print("sort".center(40, "-"))
l1 = [9, 5, 7, 1, 10, 8, 3, 6, 2, 4]
print(f"l1 :{l1}")

"""
sort    -   will sort the original list 
sorted  -   will return a copy of the sorted list
"""
res_asc = sorted(l1)
print(f"Ascending :{res_asc}")

res_desc = sorted(l1, reverse=True)
print(f"Descending :{res_desc}")

print("-" * 40)

l1 = [9,'zebra', 5, 'apple', 7, 'yellow', 1, 'blue', 10, 'violet', 8, 'green', 3, 'purple', 6, 'orange',  2, 'red', 4, 'white', 'cat', 'dog', 198, 1234, 10098, 27, 231, 2289, 20982 ]
print(f"l1 :{l1}")

print("-" * 40)
res = sorted(l1, key=ascii)
print(res)

print("-" * 40)
nl = res[12:28]

nl.sort()
print(nl)
print(f"res :{res}")
res1 = res[0:11] + nl

print("-" * 40)
print(f"res1 :{res1}")

print("-" * 40)

cities = ['kanyakumari', 'hyderabad', 'delhi', 'thiruvananthapuram', 'pune', 'bangalore', 'vishakapatnam', 'chennai', 'mumbai', 'kolkota', 'ooty']

print(f"cities :{cities}")

print("-" * 40)

res = sorted(cities, key=len)
print(f"res :{res}")

print("-" * 40)
print("-" * 40)

months = ['dec', 'jun', 'aug', 'sep', 'jan', 'nov', 'mar', 'apr', 'oct', 'feb', 'may', 'jul']

print(f"months :{months}")

# sort using sort or sorted function

from calendar import month_abbr

# print(list(month_abbr))

l = []
for mth in list(month_abbr):
    l.append(mth.lower())

def sort_months(mon):
    if mon in l:
        return l.index(mon)

res = sorted(months, key=sort_months)
print(f"res :{res}")
