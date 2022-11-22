for i in range(10):
    print(f"i is now {i}")
print()

i = 0
while i < 10:
    print(f"i={i}")
    i += 1
print()


#Modify the code so that it stops printing when it reaches a number greater than zero that's exactly divisible by 11.
# That number should be the last value printed.
# Reminder: If a value, x, is divisible by 11 then x % 11 will be zero.
for i in range(0, 100, 7):
    print(i)
    if i > 0 and i % 11 == 0:
        break
print()
# Write a program to print out all the numbers from 0 to 20 that aren't divisible by either 3 or 5.
# Zero is considered divisible by everything (zero should not appear in the output).
# The aim is to use the continue statement, but it's also possible to do this without continue.
for i in range(0, 21):
    if not(i % 3 == 0 or i % 5 == 0):
        print(i)

print()
# Game
chosen_exit = ""
available_exits = ["north", "south", "east", "west"]
while chosen_exit not in available_exits:
    chosen_exit = input("Please choose a direction ===> ")
    if chosen_exit.casefold() == "quit":
        print("Game over!")
        break
else:
    print("You got out of the room!")
