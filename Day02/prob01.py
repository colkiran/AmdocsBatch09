print("problem 9")
n=5
x=n+1
for i in range(1,n+1):
    for j in range(1,x):
        print(j,end=" ")
    print()
    if i < n:
        print(" "*i,end='')
    x=x-1

for i in range(2,n+1):
    for sp in range(n-i,0,-1):
        print(" ", end='')
    for j in range(i,0,-1):
        print(j,end=" ")
    print()

print("\n", "=" * 40, "\n")

for i in range(5, 0, -1):
    for k in range(6-i, 0, -1):
        print(" ", end="")
    for j in range(1, i+1):
        print(j, end=" ")
    print()

for i in range(2, 6):
    for k in range(6-i, 0, -1):
        print(" ", end="")
    for j in range(i, 0, -1):
        print(j, end = " ")
    print()

