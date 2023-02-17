
print("format".center(40, "-"))
# emulate c style
print("Welcome %s, what a %s player" % ("Messi", "superb"))
print("Welcome %s, with a rating of %d what a %s player" % ("Messi", 4, "superb"))
print("Welcome %s, with a rating of %.3f what a %s player" % ("Messi", 4.788992, "superb"))

print("-" * 40)
# interpolation
fname = "Lionel"
lname = "Messi"
print(f"My name is {fname} and I am known as {lname}")

print("-" * 40)
# format - python string formatting
print("Welcome {}, what a {} player".format("Messi", "class"))
print("Welcome {}, with a rating of {} what a {} player".format("Messi", 4, "class"))
print("Welcome {}, with a rating of {:.3f} what a {} player".format("Messi", 4.765834, "class"))
print("Welcome {0}, with a rating of {1:.3f} what a {2} player".format("Messi", 4.765834, "class"))
print("Welcome {2}, with a rating of {1:.3f} what a {0} player".format("Messi", 4.765834, "class"))
print("Welcome {gname}, with a rating of {rating:.3f} what a {adj} player".format(gname= "Messi", rating=4.765834, adj="class"))

print("{fn} {ln}".format(fn="Cristiano", ln="Ronaldo"))
print("{} {}".format("Cristiano", "Ronaldo"))
print("{:20} {}".format("Cristiano", "Ronaldo"))        # strings will be printed on the left
print("{:20} {}".format(7, "Ronaldo"))              # number are aligned to the right

print("-" * 40)
print("{:5} {}".format(75345345345, "Ronaldo"))              # number are aligned to the right

print("{}".format("Lionel Messi"))
print("{:.6}".format("Lionel Messi"))

print("-" * 40)


print("{:>20} {}".format("Cristiano", "Ronaldo"))   # right alignment
print("{:^20} {}".format("Cristiano", "Ronaldo"))   # center alignment
print("{:<20} {}".format("Cristiano", "Ronaldo"))   # Left alignment

print("{:->20} {}".format("Cristiano", "Ronaldo"))   # right alignment
print("{:*^20} {}".format("Cristiano", "Ronaldo"))   # center alignment
print("{:#<20} {}".format("Cristiano", "Ronaldo"))   # Left alignment
