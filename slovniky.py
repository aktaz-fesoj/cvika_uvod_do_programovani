mujprvnislovnicek = {"klic1":"hodnota1", "klic2":"hodnota2"}

slovnik = {"Jméno":"Vltava", "Délka":"400 km", "Plocha povodí":"99846226656 km2"}

print(slovnik["Jméno"])

slovnik["Plocha povodí"] = "555 km2"

print(slovnik)

for i in slovnik:
    print(i)
    
for i in slovnik.values():
    print(i)


for (key, value) in slovnik.items():          #Vrací dvojici klíč, hodnota
    print(key, value)

del slovnik["Plocha povodí"]                  #Vymazání klíče tzn i hodnoty

print(slovnik)

if "Jméno" in slovnik:
    print("Je tam!")


#Slovník je efektivnější na hledání než seznam


