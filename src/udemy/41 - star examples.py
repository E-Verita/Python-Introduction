numbers = (0,1,2,3,4,5)
print(numbers)

print(*numbers)

numb = [1,2,3,4,5,6,7]
print(*numb, sep=";")

def test_star(*args):
    print(args)
    for x in args:
        print(x)

test_star(0,1,2,3,4,5)

print()
test_star()