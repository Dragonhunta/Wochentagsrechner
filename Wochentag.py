from math import *

t = int(input("Gib den Tag ein: "))
m = int(input("Gib den Monat ein: "))
j = int(input("Gib das Jahr ein: "))

j0 = j - floor((14 - m) / 12)
m0 = m + 12 * floor((14 - m) / 12) - 2
x = j0 + floor(j0 / 4) - floor(j0 / 100) + floor(j0 / 400)
t0 = (t + x + floor((31 * m0) / 12)) % 7

print(t0)

if t0 == 0:
    print("Sonntag")
elif t0 == 1:
    print("Montag")
elif t0 == 2:
    print("Dienstag")
elif t0 == 3:
    print("Mittwoch")
elif t0 == 4:
    print("Donnerstag")
elif t0 == 5:
    print("Freitag")
elif t0 == 6:
    print("Samstag")