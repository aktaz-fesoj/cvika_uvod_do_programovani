from math import pi

pattern = "Toto je {poradi}. iterace cyklu"         #   Vypisování opakovaných textů s proměnnou
for i in range(10):
    print(pattern.format(poradi = i+1))

print(f"{pi:.3f}")                                  #   Vypíše desetinné číslo s přesností na požadovaný počet desetinných míst

a = "    Nazdár            "
print(a.strip())                                    #   Ořezává bílé znaky z obou stran
print(a.lstrip())                                   #   Zleva ořez
print(a.rstrip())                                   #   Zprava ořez

print(a.upper())                                    #   Vše uppercase
print(a.lower())                                    #   Vše lowercase

a.isdigit                                           #   Vrací 1 0
a.isnumeric

print("h" in "ahoj")

b = "Dobrý den"                                     #   Hrátky s textovým řetězcem
print(b[0])
print(b[1:])
print(b[-1])
print(b[1:3])

