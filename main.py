import time
import math

print("ez az alkalmazás képes megoldani egy másodfokú egyenletet diszkrimináns számolással")

time.sleep(1)
while True:
    a_szam = input("Kérem az A számot: ")
    try:
        a_szam = int(a_szam)
        break
    except ValueError:
        print("Ez nem egy egész szám! Próbáld Újra!")
        
while True:        
    b_szam = input("Kérem az B számot: ")
    try:
        b_szam = int(b_szam)
        break
    except ValueError:
        print("Ez nem egy egész szám! Próbáld Újra!")
        
while True:
    c_szam = input("Kérem az C számot: ")
    try:
        c_szam = int(c_szam)
        break
    except ValueError:
        print("Ez nem egy egész szám! Próbáld Újra!")

diszkriminans = (b_szam*b_szam-4*a_szam*c_szam)

print("A diszkrimináns:","|",diszkriminans,"|")

if diszkriminans < 0:
    print("Nincs valós megoldás.")
    exit()
else:
    diszkriminans > 0
    gyokszar = math.sqrt(diszkriminans)
    
if diszkriminans > 0:
    print("Kettő valós megoldás van.")
    x1 = ((-(b_szam))+gyokszar)/(2*a_szam)
    x2 = (((-b_szam))-gyokszar)/(2*a_szam)
    print("x1",x1)
    print("x2",x2)
else:
    diszkriminans == 0
    print("Egy valós megoldás van.")
    x1= (((-b_szam))+gyokszar)/(2*a_szam)
    print(x1)
