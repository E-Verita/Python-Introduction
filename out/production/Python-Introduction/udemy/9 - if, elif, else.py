import random
highest = 1000
lowest = 1
answer = random.randint(lowest, highest)
print(f"answer: {answer}") #TODO: Remove after testing
print(f"Please guess the number between {lowest} and {highest}: ")
guess = 0
while guess != answer:
    guess = int(input())
    if guess == 0:
        print("Game terminated!")
        break
    if guess < answer:
        print("Please guess higher!")
    elif guess > answer:
        print("Please guess lower!")
else:
    print("You got it!")


# if guess < answer:
#     print("Please guess higher!")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it!!")
#     else:
#         print("Sorry, you did not guessed correctly!")
# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it!!")
#     else:
#         print("Sorry, you did not guessed correctly!")
# else:
#     print("You got it right!!!")

