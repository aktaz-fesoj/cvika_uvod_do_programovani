from prevod import prevod1
while True:
    print("1 = Převod ze stupňů, minut a vteřin na desetinné číslo")
    print("2 = Převod z desetinného čísla (stupňů) na stupně, minuty a vteřiny.")
    print("0 = Ukončení programu")

    rozcesti = input()
    rozcesti = int (rozcesti)

    while rozcesti < 0 or rozcesti > 2:
        print("Toto číslo nemá svou funkci, zadej 1,2, nebo 0:")
        rozcesti = input()
        rozcesti = int (rozcesti)


    if rozcesti == 1 :
        a = input("Zadejte zeměpisnou šířku či délku:")                            #N049s 13m 37.4555v
        stupne_vstup = a[1:4]
        minuty_vstup = a[6:8]
        vteriny_vstup = a[10:-2]

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

    elif rozcesti == 2:

        while True:
            vst = input("Zadej stupně zeměpisné šířky jako desetinné číslo:")
            vst = float(vst)

        
            if vst <-180 or vst>180:
                print("Vlož číslo z intervalu <-180,180>")
                continue

            else:
                break   

        stupne = int (vst)

        minuty_des = (vst - stupne) * 60

        minuty = int (minuty_des)

        vteriny = ( minuty_des - minuty) * 60

        vteriny = round(vteriny, 3)


        print(f"{stupne}° {minuty}´ {vteriny}´´")

    elif rozcesti == 0:
        break

quit()
