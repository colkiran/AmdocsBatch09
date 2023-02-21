
print("pop".center(40, "-"))

player = {'name': 'Sachin Tendulkar', 'age': 34, 'runs': 123, 'oppn': 'Nzl'}
print(f"player :{player}")

print("-" * 40)

res = player.pop('oppn')
print(f"res :{res}")

res = player.pop('age')
print(f"res :{res}")

print(f"player :{player}")

print("popitem".center(40, "-"))

player = {'name': 'Sachin Tendulkar', 'age': 34, 'runs': 123, 'oppn': 'Nzl'}
print(f"player :{player}")

print("-" * 40)

res = player.popitem()
print(f"res :{res}")

res = player.popitem()
print(f"res :{res}")

print(f"player :{player}")

print("items".center(40, "-"))
# key, value = items()
emp = {
    'emp1': {'name': "Kevin", 'age': 34, 'desig': 'MGR', 'dept': 'MKT', 'sal': 85000},
    'emp2': {'name': "Tina", 'age': 30, 'desig': 'PL', 'dept': 'Finance', 'sal': 55000},
    'emp3': {'name': "Kenith", 'age': 28, 'desig': 'SE', 'dept': 'IT', 'sal': 40000}
}

print(f"emp :{emp}")

print("-" * 40)

print(f"emp1 :{emp['emp1']}")
print(f"emp2 :{emp['emp2']}")
print(f"emp3 :{emp['emp3']}")

print("-" * 40)

for ky, info in emp.items():
    print(ky)
    print("-" * len(ky))
    for k, v in info.items():
        print(k, "=>", v)
    print("-" * 40)

print("update".center(40, "-"))
emp1 = {'name': "Kevin", 'age': 34, 'desig': 'MGR', 'dept': 'MKT'}
emp2 =  {'name': "Tina", 'age': 30, 'desig': 'PL', 'sal': 55000}

# emp1 with emp2 values

print(f"emp1 :{emp1}")
print(f"emp2 :{emp2}")

print("-" * 40)
emp1.update(emp2)

print(f"emp1 :{emp1}")

print('clear'.center(40, "-"))
emp1  = {'name': 'Kevin', 'age': 34, 'desig': 'MGR', 'dept': 'MKT'}

print(f"emp1 :{emp1}")

emp1.clear()

print(f"emp1 :{emp1}")

