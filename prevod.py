a = input("Zadejte zeměpisnou šířku či délku:")                            #N049s 13m 37.4555v
minuty_vstup = a[6:8]
vteriny_vstup = a[10:-2]
stupne_vstup = a[1:4]
while stupne_vstup.isnumeric() == False or minuty_vstup.isnumeric() == False:
    print("Neplatný formát vstupu. Vkládejte ve formátu Nxxx° xx' xx.xxxx''")
    a = input("Zadejte zeměpisnou šířku či délku:")
    stupne_vstup = a[1:4]
    minuty_vstup = a[6:8]
    vteriny_vstup = a[10:-2]
stupne_vstup = float(stupne_vstup)
minuty_vstup = float(minuty_vstup)
vteriny_vstup = float(vteriny_vstup)
while stupne_vstup < -180 or stupne_vstup > 180 or minuty_vstup < -60 or minuty_vstup > 60 or vteriny_vstup < -60 or vteriny_vstup > 60:
    print("Neplatný formát vstupu. Vkládejte ve formátu Nxxx° xx' xx.xxxx''")
    a = input("Zadejte zeměpisnou šířku či délku:")
    stupne_vstup = a[1:4]
    minuty_vstup = a[6:8]
    vteriny_vstup = a[10:-2]
    stupne_vstup = float(stupne_vstup)
    minuty_vstup = float(minuty_vstup)
    vteriny_vstup = float(vteriny_vstup)
    
minuty_des = minuty_vstup/60
vteriny_des = vteriny_vstup/3600
stupne_vystup = stupne_vstup + minuty_des + vteriny_des
if a[0] == "N" or a[0] == "S":
    sirdel = "šířka"
else:
    sirdel = "délka"
print(f"Zeměpisná {sirdel} ve stupních v desetinném čísle je: {a[0]}{stupne_vystup:.5f}")