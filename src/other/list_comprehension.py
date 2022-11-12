# LIST COMPREHENSIONS

# standard method:
my_list = [1, 2, 3]
new_list = []
for item in my_list:
    new_list.append(item * 2)
print(my_list)
print(new_list)

my_list = [1, 2, 3]
new_list = [item * 2 for item in my_list]
print(new_list)

users = [{'name': 'Everita', 'age': 30}, {'name': 'John', 'age': 28}, {'name': 'Anna', 'age': 34}]
names = [user['name'] for user in users]
print(names)

users2 = [user['name'] for user in users if user['age'] >= 30]
print(users2)

user_groups = [
    [
        {'name': 'Everita', 'age': 30},
        {'name': 'Anna', 'age': 28},

    ],
    [
        {'name': 'John', 'age': 30},
        {'name': 'James', 'age': 34},
    ]
]

user_names = [person['name'] for group in user_groups for person in group]
print(user_names)

