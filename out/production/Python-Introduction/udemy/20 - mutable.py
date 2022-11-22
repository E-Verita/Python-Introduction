#IMUTABLE
result = "Correct"
another_result = result
print(id(result))
print(id(another_result))
result += "ish"
print(id(result))
print(id(another_result))
print()

#MUTABLE
shopping_list = ["milk", "bread", "coffee", "eggs", "cheese"]
another_list = shopping_list
print(id(shopping_list))
print(id(another_list))

print(shopping_list)
print(another_list)
shopping_list += ["cookies"]
print(shopping_list)
print(id(shopping_list))

a = b = c = e = f = another_list
print(a)
print("Adding cream")
b.append("cream")
print(c)