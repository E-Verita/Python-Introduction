panagram = "The quick brown fox jumps over the lazy dog"
words = panagram.split()
print(words)

numbers = "9,223,372,036,854,775,807"
numb_list = [int(number) for number in numbers.split(",")]
print(numb_list)

int_str = input("Please enter 3 numbers ==> ")
int_list = [int(number) for number in int_str.split(",")]
sum = 0
for number in int_list:
    sum += number
print(sum)