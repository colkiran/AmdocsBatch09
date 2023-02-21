
print("keys".center(40, "-"))
player = {'name': 'Sachin Tendulkar', 'age': 34, 'runs': 123, 'oppn': 'Nzl', 'venue': 'Auckland'}
print(f"player :{player}")

print("-" * 40)
k = player.keys()
print(k)

print("-" * 40)
for k in player.keys():
    print(k + " => " + str(player[k]))

print("values".center(40, "-"))

player = {'name': 'Sachin Tendulkar', 'age': 34, 'runs': 123, 'oppn': 'Nzl', 'venue': 'Auckland'}
print(f"player :{player}")

print("-" * 40)
v = player.values()
print(v)

print("get".center(40, "-"))
player = {'name': 'Sachin Tendulkar', 'age': 34, 'runs': 123, 'oppn': 'Nzl'}
print(f"player :{player}")

print("-" * 40)
print(f"Name  :", player.get('name', "Invalid key, please enter a valid key"))
print(f"Venue :", player.get('venue', "Invalid key, please enter a valid key"))

print("fromkeys".center(40, "-"))
cities = ['blr', 'che', 'mum', 'del', 'kol', 'hyd']
print(f"cities :{cities}")

print("-" * 40)
res = dict.fromkeys(cities)
print(f"res:{res}")

res = dict.fromkeys(cities, 24)
print(f"res :{res}")

print("-" * 40)
slno = [1, 2, 3, 4, 5]
res = dict.fromkeys(slno, ['blr', 'che', 'mum'])
print(f"res :{res}")

print("sefdefault".center(40, "-"))

player = {'name': 'Sachin Tendulkar', 'age': 34, 'runs': 123, 'oppn': 'Nzl'}
print(f"player :{player}")

print("-" * 40)
player.setdefault("name", "Sachin")
player.setdefault('age', 30)
player.setdefault('venue', 'Auckland')

print(f"player :{player}")

