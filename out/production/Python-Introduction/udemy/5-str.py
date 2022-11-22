import char as char

parrot = "Norwegian Blue"
print(parrot)
print(parrot[3])
print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])

# negative indexing
print()
print(parrot[-11])
print(parrot[-10])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])

print()
print(parrot[3-14])
print(parrot[4-14])
print(parrot[9-14])
print(parrot[3-14])
print(parrot[6-14])
print(parrot[8-14])

print()


# slice a string [:]
print(parrot[0:6])  # Norweg - not including the last character!  / up to, but not including
print(parrot[3:5])
print(parrot[:9])
print(parrot[10:])
print(parrot[:6] + parrot[6:])
print(parrot[:])
print(parrot[-4:-2])
print(parrot[-4:12])
print()

# step in a slice
print(parrot[0:6:2])  # Nre
print(parrot[0:6:3])  # Nw

number = "9,223,372,036,854,775,807"
print(number[1::4])  # ,,,,,,

number = "9,223;372:036 854,775;807"
separators = number[1::4]
print(separators)
values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])

# slice back
letters ="abcdefghijklmnopqrstuvwxyz"
backwards = letters[25:0:-1]
backwards2 = letters[25::-1]
backwards3 = letters[::-1]
print(backwards)
print(backwards2)
print(backwards3)
print(letters[16:13:-1]) # qpo
print(letters[4::-1])    # edcba
print(letters[:-9:-1])   # last 8 letters reversed

print(letters[-4:])
print





