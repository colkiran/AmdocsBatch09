
d1 = dict()
print(f"d1 :{d1}")
print(type(d1))

print("-" * 40)

d2 = {'name': 'Jack', 'age': 30, 'desig': 'BDM', 'dept': 'MKT'}
print(f"d2 :{d2}")
print(type(d2))

print("-" * 40)
d3 = dict([('name', 'Sachin'), ('age', 32), ('runs', 98), ('oppn', 'aus')])
print(f"d3: {d3}")
print(type(d3))

print("-" * 40)
d4 = dict(name="Sachin", age=32, runs=120, oppn='Nzl')
print(f"d4 :{d4}")
print(type(d4))

print("-" * 40)
# create
player = {'name': 'Sachin', 'age': 34, 'runs': 89, 'oppn': 'Nzl'}
print(f"players :{player}")

print("-" * 40)
# read
print(f"Name :{player['name']}")
print(f"Runs :{player['runs']}")

print("-" * 40)
# iterate
for x in player:
    print(x, "=>", player[x])

print("-" * 40)
# modify
player['name'] = "Sachin Tendulkar"
player['runs'] = 123
player['venue'] = 'Auckland'

print(f"player :{player}")

print("-" * 40)
# delete
del player['age']
del player['venue']

print(f"player) :{player}")

print("-" * 40)
print(dir(player))
