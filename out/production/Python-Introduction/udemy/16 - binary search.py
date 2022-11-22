import random

low = 1
high = 1000
print(f"Please think of a number between {low} and {high}")
guesses = 1

while low != high:
    guess = low + (high - low) // 2
    high_low = input(f"My guess is {guess}. Should i guess higher (h) or lower(l)? Enter c if guess was correct.")
    if high_low == "h":
        low = guess + 1
    elif high_low == "l":
        high = guess - 1
    elif high_low == "c":
        print(f"I got it in {guesses} guesses.")
        break
    else:
        print("Please enter h, l or c")
    guesses += 1
else:
    print(f"You thought of number {low}")
    print(f"I got it in {guesses} guesses.")

