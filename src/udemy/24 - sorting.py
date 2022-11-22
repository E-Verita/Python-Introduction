# SORTING - used to sort itterables (str and lists)
# .sort - changes original list, .sorted - creates a new list

pangram = "The quick brown fox jumps over the lazy dog"
letters = sorted(pangram)
print(letters)
numbers = [2.3, 4.5, 8.7, 3.1, 9.2, 1.6]
sorted_numbers = sorted(numbers)
print(numbers)
print(sorted_numbers)
another_sorted_numbers = numbers.sort()
print(numbers)
print(another_sorted_numbers)  # returns None

missing_letter = sorted("The quick brown fox jumps over the lazy dog", key=str.casefold)
print(missing_letter)

names = ["James", "John", "terry", "eric", "Terry", "michael"]
names.sort(key=str.casefold)
print(names)