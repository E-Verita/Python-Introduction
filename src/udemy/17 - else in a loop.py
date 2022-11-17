choice = "-"
while choice != "0":
    if choice in "12345":
        print(f"You choose {choice}")
    else:
        print("Please choose your option from list bellow:"
              "\n1. Learn Python"
              "\n2. Learn Java"
              "\n3. Go swimming"
              "\n4. Play chess"
              "\n5. Read a book"
              "\n0. Exit")
    choice = input()


print("*"*20)
numbers = [1, 45, 30, 12, 60]

for number in numbers:
    if number % 8 ==0:
        print("The numbers are unacceptable")       # number % 8 == 0 in the list
        break
else:
    print("All these numbers are fine.")            # number % 8 == 0 not in the list