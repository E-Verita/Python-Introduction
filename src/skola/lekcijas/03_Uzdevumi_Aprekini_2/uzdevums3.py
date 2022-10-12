# Uzrakstīt Python skriptu, kas nolasa reālu skaitli un izvada pirmo ciparu, kas atrodas pa kreisi
# no decimālās zīmes, un pirmo ciparu, kas atrodas pa labi no decimālās zīmes.
import math

x = float(input("Ievadi reālu skaitli ===> "))

a = int(x % 10)
b = int((x*10) % 10)

print(f"Cipari: {a} {b}")
