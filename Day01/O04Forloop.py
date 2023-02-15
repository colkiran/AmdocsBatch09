
for i in range(1, 10):
    print(i, end=" ")

print("-" * 40)

for i in range(1, 30):
    # if i > 20:
    #     break
    if i % 2 == 1:
        continue
    print(i, end=" ")
else:
    print("\niteration completed......")