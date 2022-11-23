n = 10
t = "e"


def sum_eo(n, t):
    if t == "e":
        total = sum(range(2, n, 2))
    elif t == "o":
        total = sum(range(1, n, 2))
    else:
        total = -1
    return total


a = sum_eo(10, "e")
print(a)

b = sum_eo(7, "o")
print(b)

c = sum_eo(11, "spam")
print(c)
