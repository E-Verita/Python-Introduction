def multiply(x: float, y: float) -> float:
    """
    Multiply 2 numbers.

    Although this function is intended to multiply 2 numbers,
    you can also use it to multiply a sequence.  If you pass
    a string, for example, as the first argument, you'll get
    the string repeated `y` times as the returned value.

    :param x: The first number to multiply.
    :param y: The number to multiply `x` by.
    :return: The product of `x` and `y`.
    """
    return x * y


answer = multiply(10, 5)
print(answer)

for val in range(1, 11):
    print(f"{val} x 10 = {multiply(val, 10)}")

def factorial(number: int) -> int:
    """
    will return the factorial of the number passed as its argument.
    """
    result = 1
    for el in range(1, number + 1):
        result *= el
    return result


for i in range(0, 36):
    print(f"{i}    i={factorial(i)}")


def is_palindrome(string: str) -> bool:
    """
    Check if a string is a palindrome.

    A palindrome is a string that reads the same forwards as backwards.

    :param string: The string to check.
    :return: True if `string` is a palindrome, False otherwise.
    """
    return string[::-1].casefold() == string.casefold()


def is_sentence_palindrome(sentence: str) -> bool:
    """
    Check if a sentence is a palindrome.

    The function ignores whitespace, capitalisation and
    punctuation in the sentence.

    :param sentence: The sentence to check.
    :return: True if `sentence` is a palindrome, False otherwise.
    """
    string = "".join([el for el in sentence if el.isalnum()])
    return is_palindrome(string)


sentence = input("Please enter sentence to check ===>")
if is_sentence_palindrome(sentence.casefold()):
    print(f"'{sentence}' is a palindorme")
else:
    print(f"'{sentence}' is not a palindorme")

word = input("Please enter word to check ===>")
if is_palindrome(word.casefold()):
    print(f"'{word}' is a palindorme")
else:
    print(f"'{word}' is not a palindorme")

answer = multiply(18, 3)
print(answer)

p = is_palindrome("test")
