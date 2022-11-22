# Viena kūka maksā a eiro un b centus. Aprēķiniet, cik eiro un cik centi jāmaksā par n kūkām
# (a, b un n veseli skaitļi).
# Uzrakstiet skriptu, kas nolasa trīs veselus skaitļus a, b un n un izvada divus veselus skaitļus:
# eiro un centus, kas jāmaksā par n kūkām

print("Ievadi kūkas cenu")
a = int(input(" eiro ===> "))
b = int(input(" centi ===> "))
n = int(input("Ievadi skaitu ===> "))
centi = (b*n) % 100
eiro = a*n + (b*n)//100
print(f"Par {n} kūkām ir jāmaksā {eiro} eiro un {centi} centi ")