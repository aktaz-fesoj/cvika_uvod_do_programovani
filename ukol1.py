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

# Vykreslení mřížky

k = 25
speed(8)
for _ in range(mrizka_x):
    for _ in range(mrizka_x):
        for _ in range(4):
            forward(k)
            left(90)
        forward(k)

    penup()
    left(180)
    forward(k * mrizka_x)
    right(90)
    forward(k)
    right(90)
    pendown()

# Podmínka, která ošetřuje různost dalšího cyklu v závislosti na počtu polí mřížky. Je-li počet polí lichý, int zaokrouhlí dolů a tak musím přičíst 1. 
# Zároveň ale přičítám k oběma variantám 1, aby vhodně fungovala fce range. Tzn. k sudým +1, k lichým +2.

if mrizka_x%2 == 0:
    pocet_tahu = int((mrizka_x*mrizka_x)/2+1)
elif mrizka_x%2 != 0:
    m = int((mrizka_x*mrizka_x)/2)
    pocet_tahu = int(m+2)

for i in range(1, pocet_tahu):         # Cyklus zajišťující konec hry po zaplnění hracího pole

    # Sběr souřadnic:

    Sour_x = numinput(f"Tah {i} hráče {hrac1}", f"{hrac1}, zvol souřadnici x svého tahu:")

    while True:
            
        if Sour_x < 1 or Sour_x > mrizka_x:         #Kontrola vstupu, prázdný vstup None je ošetřen defaultně
            Sour_x = numinput(f"Tah {i} hráče {hrac1}","Chybná souřadnice x, zadej platnou:")
            
            continue
        else:
            break

    Sour_y = numinput(f"Tah {i} hráče {hrac1}", f"{hrac1}, zvol souřadnici y svého tahu:")

    while True:
            
        if Sour_y < 1 or Sour_y > mrizka_x :        # Kontrola vstupu, prázdný vstup None je ošetřen defaultně
            Sour_y = numinput(f"Tah {i} hráče {hrac1}","Chybná souřadnice y, zadej platnou:")
            
            continue
        else:
            break

    x = Sour_x * k - k        # Jedno políčko má 10 pixelů, proto násobím. Odčítám pro to, aby kreslení začínalo v levém dolním rohu (pro 1,1 pixel 0,0)
    y = Sour_y * k - k


    # kreslení křížku na zadaných souřadnicích:
    penup()
    goto([x,y])
    pendown()
    pensize(2)
    color("blue")
    goto([x+k,y+k])
    penup()
    goto([x+k,y])
    pendown()
    goto([x,y+k])

    if i+1 == pocet_tahu and mrizka_x%2 != 0:   # Hraje-li se na lichý počet polí, program zde v posledním kole zajistí, aby nemohl hrát hráč 2, který už by neměl volné pole.
        break



    Sour2_x = numinput(f"Tah {i} hráče {hrac2}", f"{hrac2}, zvol souřadnici x svého tahu:")

    while True:
            
        if Sour2_x < 1 or Sour2_x > mrizka_x :      #Kontrola vstupu, prázdný vstup None je ošetřen defaultně
            Sour2_x = numinput(f"Tah {i} hráče {hrac2}","Chybná souřadnice x, zadej platnou:")
            
            continue
        else:
            break

    Sour2_y = numinput(f"Tah {i} hráče {hrac2}", f"{hrac2}, zvol souřadnici y svého tahu:")

    while True:
            
        if Sour2_y < 1 or Sour2_y > mrizka_x :      #Kontrola vstupu, prázdný vstup None je ošetřen defaultně
            Sour2_y = numinput(f"Tah {i} hráče {hrac2}","Chybná souřadnice y, zadej platnou:")   
                
            continue
        else:
            break

    x2 = Sour2_x * k - (k/2) # Násobení k <- jedno pole k pixelů, minus k/2 a minus 0,9k tak, aby kreslení kružnice začínalo v prostředku při dolním okraji pole (lehce odsazené o 0,1k px).
    y2 = Sour2_y * k - (0.9*k)


    # kreslení kolečka na zadaných souřadnicích:
    penup()
    goto([x2,y2])
    pendown()
    pensize(2)
    color("red")
    circle(0.4*k,360)













