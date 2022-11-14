choice = int(input("Please choose your option from list bellow:"
      "\n1. Learn Python"
      "\n2. Learn Java"
      "\n3. Go swimming"
      "\n4. Play chess"
      "\n5. Read a book"
      "\n0. Exit"))

while choice != 0:
    if choice == 1:
        print("1")
    choice = input()






numbers = [1, 45, 30, 12, 60]

for number in numbers:
    if number % 8 ==0:
        print("The numbers are unacceptable")       # number % 8 == 0 in the list
        break
else:
    print("All these numbers are fine.")            # number % 8 == 0 not in the list