# LIST COMPREHENSIONS
# Let's learn about list comprehensions! You are given three integers  and  representing the dimensions of a cuboid along with an integer .
# Print a list of all possible coordinates given by (i, j, k) on a 3D grid where the sum of i +j +k  is not equal to n.
# Here 0 <= i <= x; 0 <= j <= y; 0 <= k <= z;  Please use list comprehensions rather than multiple loops, as a learning exercise.
""""
Sample Input 0
1
1
1
2
Sample Output 0
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

Sample Input 1
2
2
2
2
Sample Output 1
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 2], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]]

"""

x = int(input("x ===> "))
y = int(input("y ===> "))
z = int(input("z ===> "))
n = int(input("n ===> "))

permutations = []

for i in range(0, x+1):
    for j in range(0, y + 1):
        for k in range (0, z + 1):
            if i + j + k != n:
                xlist =[i, j, k]
                print(xlist)
                permutations.append(xlist)
print(permutations)


































print("\n\n\n")
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

