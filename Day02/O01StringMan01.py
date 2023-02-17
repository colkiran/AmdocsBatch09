
st = "hello world"
print(f"st :{st}")
print(type(st))

print("-" * 40)
# strings are immutable

print(f"st[0]  :{st[0]}")        # strings are stored like list (Array)
# st[0] = "H"
print(f"st[6]  :{st[6]}")
print(f"st[10] :{st[10]}")

print("-" * 40)
# slicing
print(f"st[0:5]  :{st[0:5]}")
print(f"st[6:11] :{st[6:11]}")
print(f"st[0:11] :{st[0:11]}")
print(f"st[0:]   :{st[0:]}")
print(f"st[:11]  :{st[:11]}")
print(f"st[:]    :{st[:]}")

print("-" * 40)
# reverse indexing
print(f"st[-1]  :{st[-1]}")
print(f"st[-7]  :{st[-7]}")
print(f"st[-11] :{st[-11]}")

print("-" * 40)
# slicing
print(f"st[-1: -6: -1]  :{st[-1: -6: -1]}")
print(f"st[-7: -12: -1] :{st[-7: -12: -1]}")
print(f"st[1-: -12: -1] :{st[-1: -12: -1]}")
print(f"st[-1: :-1]     :{st[-1: :-1]}")
print(f"st[:-12: -1]    :{st[:-12: -1]}")
print(f"st[::-1]        :{st[::-1]}")

print("-" * 40)
# write a code to check if the given string is a palindrome
str = "malayalam"
print(f"palindrome {str}" if (str == str[::-1]) else f"Not a palindrome {str[::-1]}")

if (str == str[::-1]):
    print("it is palindrome")
else:
    print("it is not palindrome")

print("-" * 40)
print(dir(st))
