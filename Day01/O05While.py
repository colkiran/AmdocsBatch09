
x = 1
while x <= 10:
    print(x, end=" ")
    x += 1
print()

print(f"outside :{x}")

while True:
    if x < 1:
        break
    print(x, end=" ")
    x -= 1
