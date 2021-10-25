from math import sqrt

a = input("Zadej koeficient a:")
a = float(a)
b = input("Zadej koeficient b:")
b = float(b)
c =input("Zadej koeficient c:")
c = float(c)


D = (b**2 - 4*a*c)

if D < 0:
   
    print("Rovnice nemá kořen v oboru reálných čísel, záporný diskriminant.")
    

elif D == 0:

    D2 = sqrt(D)
    
    koren1 = (-b- D2)/(2*a)
    koren2 = (-b+ D2)/(2*a)
    print("Rovnice má dvojnásobný kořen ", koren1, ".")
    

else:

    D2 = sqrt(D)

    koren1 = (-b- D2)/(2*a)
    koren2 = (-b+ D2)/(2*a)
    print("Kořeny kvadratické rovnice jsou", koren1, "a", koren2, ".")

