even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

empty_list = []

numbers = [even, odd]
print(numbers)

for number_list in numbers:
    print(number_list)
    for value in number_list:
        print(value)

print("*"*20)


numbers = even + odd
print(numbers)

sorted_numbers = sorted(numbers)
print(numbers)
print(sorted_numbers)

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]


digits = sorted("564764482")
print(digits)  # ['2', '4', '4', '4', '5', '6', '6', '7', '8']
digit_list = list("156464321")
print(digit_list)
print([int(el) for el in digit_list])
print()
more_numbers = numbers.copy()
print(more_numbers)
print(id(numbers))
print(id(more_numbers))
print("*"*20)
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
print(min(even))
print(max(odd))

print(len(odd))
print()
print("mississippi".count("iss"))

even.extend(odd)
print(even)
another_even = even
print(another_even)

even.sort()
print(even)
even.sort(reverse=True)
print(even)
print(another_even)