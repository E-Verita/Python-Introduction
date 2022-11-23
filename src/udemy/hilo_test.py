LOW = 1
HIGH = 6553500


def guess_binary(answer, low, high):
    guesses = 1
    while True:
        guess = low + (high - low) // 2
        if guess < answer:
            low = guess + 1
        elif guess > answer:
            high = guess - 1
        elif guess == answer:
            return guesses

        guesses += 1

correct_count = 0
max_guesses = 0
for number in range(LOW, HIGH + 1):
    number_of_guesses = guess_binary(number, LOW, HIGH)
    print(f"{number} guessed in {number_of_guesses}")

    if number_of_guesses > max_guesses:
        max_guesses, correct_count = number_of_guesses, 1
    elif number_of_guesses == max_guesses:
        correct_count += 1
print(f"I guessed without beeing told {correct_count} times. Max {max_guesses} guesses.")

"""
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
    
"""
