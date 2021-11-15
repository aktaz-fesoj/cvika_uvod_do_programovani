#Program má seznam měst, jedno vybere, pak se ptá na písmenka -> šibenice
import random

mesto = random.choice(["Praha", "Brno", "Kolín", "Lípa", "Rumburk", "Jestřebí", "Pacov"])
mesto = mesto.lower()
mesto_list = list(mesto)
delka_slova = len(mesto_list)

Hadane = []
for i in range(delka_slova):
        Hadane.extend("_")

while mesto_list != Hadane:
    pismeno = input("Zadej písmeno:")

    for i in range(delka_slova):
        if pismeno in mesto_list[i]:
            if i == 0:
                Hadane[i] = pismeno.upper()
            else:
                Hadane[i] = pismeno
    if pismeno in mesto_list:
        print("Trefa!")
        print (*Hadane, sep = " ")   #TOJEONO
    else:
        print("To není ono :(")

print("Je to doma! Dokázal jsi uhodnout hledané město!")




            
