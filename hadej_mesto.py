#Program má seznam měst, jedno vybere, pak se ptá na písmenka -> šibenice
import random
import csv

seznam_okresnich_mest = []
with open("okresni_mesta.csv", encoding = "utf-8") as mesta_csv:
    reader = csv.reader(mesta_csv,)
    for row in reader:
      seznam_okresnich_mest.append(row[0])  

mesto = random.choice(seznam_okresnich_mest)
mesto_list_kontrola = list(mesto)
mesto_1 = mesto.lower()
mesto_list = list(mesto_1)

delka_slova = len(mesto_list)

hadane = []
for i in range(delka_slova):
    hadane.extend("_")

for i in range(delka_slova):
    if mesto_list[i] == " ":
        hadane[i] = " "

while mesto_list_kontrola != hadane:
    pismeno = input("Zadej písmeno:").lower()

    for i in range(delka_slova):
        if pismeno == mesto_list[i]:
            if i == 0:
                hadane[i] = pismeno.upper()
            else:
                hadane[i] = pismeno
            if mesto_list[i-1] == " ":
                mesto_list_kontrola[i] = pismeno.lower()
    if pismeno in mesto_list:
        print("Trefa!")
        print (*hadane, sep = " ")
    else:
        print("To není ono :(")
        print (*hadane, sep = " ")

print("Je to doma! Dokázal jsi uhodnout hledané město!")
exit()