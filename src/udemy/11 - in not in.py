name = input("What is your name? ")
age = int(input("What is your age? "))
if 18 <= age <= 30:
    print(f"Welcome on the holiday, {name}!")
else:
    print(f"Sorry {name}, no holiday for a person in a age of {age}")

print("*"*80)

activity = input("What would you like to do today? ")
if "cinema" not in activity.casefold():
    print("But I want to go to cinema!")

print("*"*80)

parrot = "Norwegian Blue"

letter = input("Enter a character: ")
if letter in parrot:
    print(f"{letter} is in {parrot}")
else:
    print("I don't need that letter!")

