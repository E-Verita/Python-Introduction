def multiply(a, b):
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
    return a * b


answer = multiply(10, 5)
print(answer)

for val in range(1, 11):
    print(f"{val} x 10 = {multiply(val, 10)}")


def is_palindrome(string):
    """
    Check if a string is a palindrome.

    A palindrome is a string that reads the same forwards as backwards.

    :param string: The string to check.
    :return: True if `string` is a palindrome, False otherwise.
    """
    return string[::-1].casefold() == string.casefold()


def is_sentence_palindrome(sentence):
    """
    Check if a sentence is a palindrome.

    The function ignores whitespace, capitalisation and
    punctuation in the sentence.

    :param sentence: The sentence to check.
    :return: True if `sentence` is a palindrome, False otherwise.
    """
    string = "".join([el for el in sentence if el.isalnum() == True])
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

answer = multiply(18,3)
print(answer)