print("1 = Převod ze stupňů, minut a vteřin na desetinné číslo")
print("2 = Převod z desetinného čísla (stupňů) na stupně, minuty a vteřiny.")

while True:
    rozcesti = input()
    rozcesti = int (rozcesti)
    if rozcesti < 1 or rozcesti > 2:
        print("Toto číslo nemá svou funkci, zadej 1 nebo 2:")
        continue
    else:
        break





if rozcesti == 1 :
    while True:
        
        a = input("Zadejte stupně:")
        stupne_vstup = float(a)
        if stupne_vstup < -180 or stupne_vstup > 180 :
            print("Vlož číslo z intervalu <-180,180>")
            continue
        else:
            break
    
    while True:        
        b = input("Zadejte minuty:")
        minuty_vstup = float(b)
        if minuty_vstup < -60 or minuty_vstup > 60 :
            print("Vlož číslo z intervalu <-60,60>")
            continue
        else:
            break
        

    while True:        
        c =input("Zadejte vteřiny:")
        vteriny_vstup = float(c)
        if vteriny_vstup < -60 or vteriny_vstup > 60 :
            print("Vlož číslo z intervalu <-60,60>")
            continue
        else:
            break

    minuty_des = minuty_vstup/60

    vteriny_des = vteriny_vstup/3600

    stupne_vystup = stupne_vstup + minuty_des + vteriny_des

    print(stupne_vystup)

elif rozcesti == 2:

    while True:
        vst = input("Zadej stupně jako desetinné číslo:")
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


    print(stupne , "° " , minuty , "´ " , vteriny , "´´")