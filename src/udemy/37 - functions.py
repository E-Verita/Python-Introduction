def multiply(a, b):
    return a * b


answer = multiply(10, 5)
print(answer)

for val in range(1, 11):
    print(f"{val} x 10 = {multiply(val, 10)}")


def is_palindrome(string):
    return string[::-1] == string


def is_sentence_palindrome(string):
    string = "".join([el for el in string if el.isalnum() == True])
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
