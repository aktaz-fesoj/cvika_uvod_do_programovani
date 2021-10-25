from turtle import *

# Název okna:
title("Pišqworky od Pepy verze 1.0")

# Nastavení hráčů:
hrac1 = textinput("Začátek hry!","Zadej jméno prvního hráče:")

while True:
        
    if hrac1 == "" :        # Kontrola vstupu. Pokud uživatel potvrdí jméno bez zadání znaku, bude vyzván opětovnému zadání.
        hrac1 = textinput("Chyba","Chyba, zadej platné jméno prvního hráče:")
        
        continue
    else:
        break

hrac2 = textinput("Začátek hry!","Zadej jméno druhého hráče:")

while True:
        
    if hrac2 == "" or hrac1 == hrac2 : # Kontrola vstupu. Pokud uživatel potvrdí jméno bez zadání znaku, či se bude jméno shodovat s prvním, bude vyzván opětovnému zadání.
        hrac2 = textinput("Chyba","Chyba, zadej platné jméno druhého hráče:")
        
        continue
    else:
        break

# Nastavení mřížky:
mrizka_x = numinput("Začátek hry!","Na čtverci o kolika polích byste chtěli hrát?")

while True:
        
    if mrizka_x < 3 or mrizka_x > 20 :
        mrizka_x = textinput("Chyba","Chyba, zadejte rozměr mezi 3 a 20:")
        
        continue
    else:
        break


mrizka_x = int(mrizka_x)

# Vykreslení mřížky, zvolil jsem šiřku a výšku jednoho pole na 10 px:
speed(4)
for _ in range(mrizka_x):
    for _ in range(mrizka_x):
        for _ in range(4):
            forward(10)
            left(90)
        forward(10)

    penup()
    left(180)
    forward(10*mrizka_x)
    right(90)
    forward(10)
    right(90)
    pendown()


while True:         # Nekonečný cyklus, tak aby hráči hru sami ukončili až zavřením grafického okna

    # Sběr souřadnic:

    Sour_x = numinput(f"Tah hráče {hrac1}", f"{hrac1}, zvol souřadnici x svého tahu:")

    while True:
            
        if Sour_x < 1 or Sour_x > mrizka_x:         #Kontrola vstupu, prázdný vstup None je ošetřen defaultně
            Sour_x = numinput(f"Tah hráče {hrac1}","Chybná souřadnice x, zadej platnou:")
            
            continue
        else:
            break

    Sour_y = numinput(f"Tah hráče {hrac1}", f"{hrac1}, zvol souřadnici y svého tahu:")

    while True:
            
        if Sour_y < 1 or Sour_y > mrizka_x :        # Kontrola vstupu, prázdný vstup None je ošetřen defaultně
            Sour_y = numinput(f"Tah hráče {hrac1}","Chybná souřadnice y, zadej platnou:")
            
            continue
        else:
            break

    x = Sour_x * 10 - 10        # Jedno políčko má 10 pixelů, proto násobím. Odčítám pro to, aby kreslení začínalo v levém dolním rohu (pro 1,1 pixel 0,0)
    y = Sour_y * 10 - 10


    # kreslení křížku na zadaných souřadnicích:
    penup()
    goto([x,y])
    pendown()
    pensize(2)
    color("blue")
    goto([x+10,y+10])
    goto([x+10,y])
    goto([x,y+10])



    Sour2_x = numinput(f"Tah hráče {hrac2}", f"{hrac2}, zvol souřadnici x svého tahu:")

    while True:
            
        if Sour2_x < 1 or Sour2_x > mrizka_x :      #Kontrola vstupu, prázdný vstup None je ošetřen defaultně
            Sour2_x = numinput(f"Tah hráče {hrac2}","Chybná souřadnice x, zadej platnou:")
            
            continue
        else:
            break

    Sour2_y = numinput(f"Tah hráče {hrac2}", f"{hrac2}, zvol souřadnici y svého tahu:")

    while True:
            
        if Sour2_y < 1 or Sour2_y > mrizka_x :      #Kontrola vstupu, prázdný vstup None je ošetřen defaultně
            Sour2_y = numinput(f"Tah hráče {hrac2}","Chybná souřadnice y, zadej platnou:")   
                
            continue
        else:
            break

    x2 = Sour2_x * 10 - 5 # Násobení deseti <- jedno pole 10 pixelů, minus 5 a minus 9 tak, aby kreslení kružnice začínalo v prostředku na dolním okraji pole (lehce odsazené o 1 pixel).
    y2 = Sour2_y * 10 - 9


    #kreslení kolečka na zadaných souřadnicích:
    penup()
    goto([x2,y2])
    pendown()
    pensize(2)
    color("red")
    circle(4,360)











