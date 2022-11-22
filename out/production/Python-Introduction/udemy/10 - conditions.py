if 0:
    print("True")
else:
    print("False")

name = input("Please enter your name: ")
if name:
    print(f"Hello, {name}")
else:
    print("Do you have no name?")

print("-"*80)

day = "Saturday"
temperature = 30
raining = True
if day == "Saturday" and temperature > 27 or not raining:
    print("Go swimming")
else:
    print("Learn Python")

print("-"*80)

age = int(input("How old are you?"))
if 16 <= age <= 65:
    print("Have a good day at work!")
else:
    print("Enjoy your free time")



