
# find and replace
st1 = "hello world"
st2 = "the quick brown fox jumps over the lazy dog"

print(f"st1 :{st1}")
res = st1.find("w")
print(f"res: {res}")

res = st1.find("l", st1.find("l", st1.find("l")+1)+1)
print(f"res: {res}")

print("-" * 40)

print(f"st2 :{st2}")
res = st2.find("fox")
print(f"res: {res}")

res = st2.find("the", st2.find("the")+1)
print(f"res :{res}")

print("replace".center(40, "-"))
st1 = "hello world"
st2 = "the quick brown fox jumps over the lazy dog"

print(f"st1 :{st1}")
res = st1.replace("h", "H")
print(f"res :{res}")

res = st1.replace("l", "L", 1)
print(f"res :{res}")

print("-" * 40)
print(f"st2 :{st2}")
res = st2.replace("brown fox", "white tiger")
print(f"res :{res}")

res = st2.replace("the", "The", 1)
print(f"res :{res}")

# maketrans, translate
print("maketrans".center(40, "-"))
st = 'hello world'
print(f"st :{st}")

a = 'helowrd'
b = 'HELOWRD'
# length of a and b should be the same
print(f"a :{a}")
print(f"b :{b}")

resTbl = st.maketrans(a, b)
print(f"resTbl :{resTbl}")

print("translate".center(40, "-"))
res = st.translate(resTbl)
print(f"res :{res}")
