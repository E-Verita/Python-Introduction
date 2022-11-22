# Uzrakstīt Python skriptu, kas nolasa reālu skaitli ar diviem decimālajiem cipariem un pēc tam
# izvada šī skaitļa decimālās daļas vērtību.
# Uzdevuma risinājumā izmantojiet aritmētiskus aprēķinus

x = float(input("Ievadi reālu skaitli ar diviem decimālajiem cipariem ===> "))
decimala = float(x % 1)
print(f"Decimālā daļa ir: {decimala:.2f}")
