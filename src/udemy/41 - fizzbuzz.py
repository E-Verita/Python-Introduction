def fizz_buzz (number: int) -> str:
    """
    If the number is divisible by 3, returns "fizz".
    If the number is divisible by 5, returns "buzz".
    If the number is divisible by 3 and 5, returns "fizz buzz".

    """
    if number % 15 == 0:
        return "fizz buzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    else:
        return str(number)


input("Play Fizz Buzz. Press ENTER to start")
print()

next_number = 0
while next_number < 99:
    next_number += 1
    print(fizz_buzz(next_number))
    next_number += 1
    correct_answer = fizz_buzz(next_number)
    players_answer = input("You go: ")
    if players_answer != correct_answer:
        print(f"You loose, correct answer was {correct_answer}")
        break
else:
    print(f"Well done! You reached {next_number}")
