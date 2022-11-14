numbers = [1, 45, 30, 12, 60]

for number in numbers:
    if number % 8 ==0:
        print("The numbers are unacceptable")       # number % 8 == 0 in the list
        break
else:
    print("All these numbers are fine.")            # number % 8 == 0 not in the list