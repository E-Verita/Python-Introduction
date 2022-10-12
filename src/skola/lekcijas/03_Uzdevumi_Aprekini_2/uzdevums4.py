# Uzrakstīt Python skriptu, kas nolasa reālu skaitli ar diviem decimālajiem cipariem un pēc tam
# izvada šī skaitļa decimālās daļas vērtību.
# Uzdevuma risinājumā izmantojiet aritmētiskus aprēķinus

x = input("Ievadi reālu skaitli ar diviem decimālajiem cipariem ===> ")
decimala = (float(x)*100)%100/100
print(f"Decimālā daļa ir: {decimala:.2f}")