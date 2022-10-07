# concatenate
string1 = "he's "
string2 = "probably "
string3 = "pining "
string4 = "for "
string5 = "the fjords "
print(string1 + string2 + string3 + string4 + string5)
print("Hello " * 5)
print("Hello " * (5 + 4))
print("Hello " * 5 + "4")

# contains
today = "friday"
print("day" in today)  # True
print("fri" in today)  # True
print("mon" in today)  # False

# replacement
age = 31
print("My age is " + str(age) + " years")
print("My age is {0} years".format(age))
print("There are {0} days in {1}, {2}, {3}, and {4}"
      .format(30, "Apr", "Jun", "Sept", "Nov"))

# formatting

for i in range(1, 13):
    print("N.{0} squared is {1} and cubed is {2}".format(i, i ** 2, i ** 3))
print()
for i in range(1, 13):
    print("N.{0:2} squared is {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 3))
print()

for i in range(1, 13):
    print("N.{0:2} squared is {1:<3} and cubed is {2:<4}".format(i, i ** 2, i ** 3))
print()

for i in range(1, 13):
    print("N.{0:2} squared is {1:<3} and cubed is {2:^4}".format(i, i ** 2, i ** 3))
print()

# f-strings
name = "Everita"
balance = 125,25
print(name + f" has {balance} in her account")

# interpolation
number = 24
print("My age is %d years" % age)
major = "years"
minor = "months"
print("My age is %d  %s, %d %s" % (number, major,6, minor))
pi = 22/7
print("Pi is %.2f" % (22/7))
