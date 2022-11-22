import random
import math

sx = []
sy =[]
for i in range(10):
    i = random.randint(-10,10)
    j = random.randint(-10,10)
    sx.append(i)
    sy.append(j)
sx = [-2, -2, -6, -7, -10, -2, -3, -2, -9, -8]
sy = [-10, -6, -7, -8, -8, -8, 0, -3, -2, -3]

print(f"1. Ģenerētie saraksti:\n{sx}\n{sy}")

print("\n2. Koordinātu pāri:")
for i in range(0, len(sx)):
    print(f"{sx[i]}, {sy[i]}")

minx = sx[0]
maxx = sx[0]
miny = sy[0]
maxy = sy[0]

for i in range(1, len(sx)):
    if sx[i] > maxx:
        maxx = sx[i]
    if sx[i] < minx:
        minx = sx[i]
    if sy[i] > maxy:
        maxy = sy[i]
    if sy[i] < miny:
        miny = sy[i]

print(f"\n3. Mazākā taisnstūra stūru punktu koordinātu pāri:")
print(f"({minx}, {miny}), ({minx}, {maxy}), ({maxx}, {maxy}), ({maxx}, {miny})")

if maxx < 0 and maxy < 0:
    laukums = abs(minx + abs(maxx)) * abs(miny + abs(maxy))
elif maxx < 0:
    laukums = abs(minx + abs(maxx)) * (abs(miny) + abs(maxy))
elif maxy < 0:
    laukums = (abs(minx) + abs(maxx)) * abs(miny + abs(maxy))
else:
    laukums = (abs(minx) + abs(maxx)) * (abs(miny) + abs(maxy))
print(f"\n4. Taisnstūra laukums: {laukums} ")

x = random.randint(-10, 10)
y = random.randint(-10, 10)

if maxx >= x >= minx and maxy >= y >= miny:
    if x == maxx or x == minx or y == miny or y == maxy:
        if x == maxx:
            if y == miny:
                vieta = "apakšējais labais stūris"
            elif y == maxy:
                vieta = "augšējais labais stūris"
            else:
                vieta = "labā mala"

        elif x == minx:
            if y == miny:
                vieta = "apakšējais kreisais stūris"
            elif y == maxy:
                vieta = "augšējais kreisais stūris"
            else:
                vieta = "kreisā mala"

        elif y == miny:
            vieta = "apakšējā mala"

        elif y == maxy:
            vieta = "apakšējā mala"
    else:
        vieta = "iekšiene"
else:
    vieta = "ārpuse"
print(f"\n5. Ģenerēts punkts ({x}, {y}) un tā atrašanās vieta ir taisnstūra {vieta}. ")

ax = 0
ay = 0

if maxx > abs(minx):
    ax = maxx
else:
    ax = abs(minx)

if maxy > abs(miny):
    ay = abs(maxy)
else:
    ay = abs(miny)

if ax == ay:
    print("VIENĀDI!")
    x = 0
    y = 0
    for i in range(0, len(sx)):
        if abs(sx[i]) == ax:
            if abs(sy[i]) > y:
                y = abs(sy[i])

    for i in range(0, len(sy)):
        if abs(sy[i]) == ay:
            if abs(sx[i]) > x:
                x = abs(sx[i])
    if x > y:
        ax = x
    else:
        ay = y

elif ax > ay:
    ay = 0
    for i in range(0, len(sx)):
        if abs(sx[i]) == ax:
            if abs(sy[i]) > ay:
                ay = abs(sy[i])

else:
    ax = 0
    for i in range(0, len(sy)):
        if abs(sy[i]) == ay:
            if abs(sx[i]) > ax:
                ax = abs(sx[i])

print(f"ax={ax}, ay={ay}")

#pitagora teorēma
a = ax
b = ay
c = math.sqrt(a**2 + b**2)  # = Radiuss (tālākā punkta attālums līdz (0, 0))

print(f"\n6. Riņķa līnijas rādius ir {c:.4f} un laukums ir {math.pi*c**2:.4f} ")