for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
print()

#ver 1:
shopping = ["milk", "bread", "coffee", "tea", "cheese"]
item_to_find = "albatross"
found_at = None
for index in range(len(shopping)):
    if shopping[index] == item_to_find:
        found_at = index
        break                                   # we don't need the loop to continue after we have found it
if found_at is not None:
    print(f"{item_to_find.capitalize()} found at {found_at}")
else:
    print(f"{item_to_find.capitalize()} not found!")

#ver 2:
shopping = ["milk", "bread", "coffee", "tea", "cheese"]
item_to_find = "ice"
found_at = None

if item_to_find in shopping:
    found_at = shopping.index(item_to_find)

if found_at is not None:
    print(f"{item_to_find.capitalize()} found at {found_at}")
else:
    print(f"{item_to_find.capitalize()} not found!")