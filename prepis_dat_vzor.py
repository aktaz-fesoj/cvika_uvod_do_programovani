#ČTENÍ
with open("D:\\GEKA\\2. ZS\\Úvod do programování cvika\\pokusna_data.txt", encoding = "utf-8") as f:    #f může bát cokolov jiného -jiná proměnná
    obsah = f.read()
    print(obsah)

    #for radek in f:
    #   print(f"ŘÁDEK: {radek}")

#ZÁPIS (do dosud neexistujícího souboru - ten jsem vytvořil)
with open("D:\\GEKA\\2. ZS\\Úvod do programování cvika\\pokusna_data_out.txt", mode="w", encoding = "utf-8") as f:
    f.write("Ahoj")

