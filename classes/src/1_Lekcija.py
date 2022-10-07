# id
import math

print(type(5))
print(id(5))
a = 5
b = 5

print(id(a))
print(id(b))
print(a + b)
print(id(a + b))

# nosaukumi

preces_cena = 1.235
prece_01 = 'banāns'
KONSTANTE = 3, 14  # var izmainīt, bet nevajag

c = (1 + 2 + 3
     + 4 + 5 + 6)

d = (1 + 2) * (3 * 4)
e = 1 * 2 + 4 * 3
f = a * 2 - 1
print(c)

# print(f"{}")

print(f"prece = {prece_01}, preces_cena = {preces_cena}")

# :.2f
print(f"prece = {prece_01}, preces_cena = {preces_cena:.1f}")

# round
print(f"prece = {prece_01}, preces_cena = {round(preces_cena,2)}")

# len
print(len("Hello"))


# str --> float ---> int  (nevar str --> int)

g = 12
print(g)
h = str(g)
print(h)
i = float(h)
print(i)
j = int(i)
print(j)
print()


#input and { }

m = int(input("Ievadi m:"))
n = int(input("Ievadi n:"))

print(f"{m} + {n} = ", m + n)
print(f"{m} * {n} = ", m * n)
print(f"{m} / {n} = ", m / n)
print(f"{m} // {n} = ", m // n)

# if "import math"
print(f"kvadrātsakne no {m} = {math.sqrt(m)}")
print(f"kvadrātsakne no {n} = {math.sqrt(n)}")
print(f"kvadrātsakne no {m} ar 2 cipariem aiz komata = {math.sqrt(m):.2f}")

# if "from math import sqrt" :  print(f"kvadrātsakne no {n} = {sqrt(n)}")









