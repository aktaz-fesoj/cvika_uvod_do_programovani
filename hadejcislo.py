from random import randrange

nahcislo = randrange(1,100)


while True:

    cislo = input("Hádej číslo:")
    cislo = int(cislo)
    if cislo != nahcislo :
        print("To není ono!")
        if nahcislo < cislo:
            print("Hledané číslo je menší!")
        elif nahcislo > cislo:
            print("Hledané číslo je větší!")
        continue
    else:
        break

print("Uhádnuls tos! Gratuluju.")
quit()

