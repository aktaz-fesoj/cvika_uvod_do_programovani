#Program má seznam měst, jedno vybere, pak se ptá na písmenka -> šibenice
import random

mesto = random.choice(["Praha", "Brno", "Kolín", "Lípa", "Rumburk", "Jestřebí", "Pacov"])
pismeno = input("Zadej písmeno:")

mesto_list = list(mesto)
delka_slova = len(mesto_list)
print(mesto_list)

Hadane = []
for i in range(delka_slova):
    Hadane.extend("_")
for i in range(delka_slova):
    if pismeno in mesto_list[i]:
        Hadane[i] = pismeno

print (*Hadane, sep = "")   #TOJEONO


            
