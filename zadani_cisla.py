def ZadejCeleCislo(retezec):
    while True:
        try:
            cislo = int(input(f"{retezec}"))
            print(f"Číslo je {cislo}")            
            return(cislo)
        except ValueError:
            print("Nebylo zadáno celé číslo")
            
mojecislo = ZadejCeleCislo("Zadejte číslo tralalala:")

print(f"Toto je moje cislo:{mojecislo}")