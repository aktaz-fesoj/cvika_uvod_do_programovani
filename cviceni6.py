### VÝJIMKY ###

try:
    val = int(input("Zadej cislo:"))
except ValueError:
    print("Nebylo zadáno číslo")
    exit()

else:#když nenastane vyjimka
    pass
finally:
    pass

print(f"bylo zadáno číslo {val}")
