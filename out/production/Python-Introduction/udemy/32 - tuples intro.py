t = "a", "b", "c"
print(t)

name = "Everita"
age = 31
print(name, age, "Python", 2022)
print((name, age, "Python", 2022))
print()

# TUPLES - sequence type, immutable
# use less memory than list
# can be used to protect the integrity of data

welcome = "Welcome ro my Nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the Lightning", "Metalica", 1984
print(metallica)
print(metallica[0])
print(metallica[1])
print(metallica[2])

metallica2 = list(metallica)
print(metallica2)

metallica2[0] = "Master of Puppets"
print(metallica2)
