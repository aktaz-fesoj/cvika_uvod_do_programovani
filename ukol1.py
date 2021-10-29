from turtle import forward, right, left, textinput, numinput, title, speed, color, goto, penup, pendown, pensize, circle

# Název okna:
title("Pišqworky od Pepy verze 1.1")

# Nastavení hráčů:
hrac1 = textinput("Začátek hry!","Zadej jméno prvního hráče:")

# Kontrola vstupu. Pokud uživatel potvrdí jméno bez zadání znaku, bude vyzván k opětovnému zadání:
while True:
        
    if hrac1 == "" :        
        hrac1 = textinput("Chyba","Chyba, zadej platné jméno prvního hráče:")
        
        continue
    else:
        break

hrac2 = textinput("Začátek hry!","Zadej jméno druhého hráče:")

# Kontrola vstupu. Pokud uživatel potvrdí jméno bez zadání znaku, či se bude jméno shodovat s prvním, bude vyzván k opětovnému zadání:
while True:
        
    if hrac2 == "" or hrac1 == hrac2 : 
        hrac2 = textinput("Chyba","Chyba, zadej platné jméno druhého hráče:")
        
        continue
    else:
        break

# Nastavení mřížky:

mrizka_x = numinput("Začátek hry!","Na mřížce o kolika polích byste chtěli hrát?")

while True:

    mrizka_kontrola  = mrizka_x % 1 #Zbytek z celočíselného dělení, v podmínce níže, kontoluji, jestli je zbytkem nula, jinak bylo zadáno desetinné číslo = neplatný rozměr mřížky.
        
    if mrizka_x < 3 or mrizka_x > 20 or mrizka_kontrola != 0:
        mrizka_x = numinput("Chyba","Chyba, zadejte celočíselný rozměr mezi 3 a 20:")
        
        continue
    else:
        break


mrizka_x = int(mrizka_x)

# Vykreslení mřížky

k = 25   #Konstanta určující velikost pole mřížky.

speed(0)
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
            
        if Sour_x < 1 or Sour_x > mrizka_x or Sour_x%1 != 0 :         #Kontrola vstupu, prázdný vstup None je ošetřen defaultně
            Sour_x = numinput(f"Tah {i} hráče {hrac1}","Chybná souřadnice x, zadej platnou:")
            
            continue
        else:
            break

    Sour_y = numinput(f"Tah {i} hráče {hrac1}", f"{hrac1}, zvol souřadnici y svého tahu:")

    while True:
            
        if Sour_y < 1 or Sour_y > mrizka_x or Sour_y%1 != 0 :        # Kontrola vstupu, prázdný vstup None je ošetřen defaultně
            Sour_y = numinput(f"Tah {i} hráče {hrac1}","Chybná souřadnice y, zadej platnou:")
            
            continue
        else:
            break

    x = Sour_x * k - k        # Jedno políčko má k pixelů, proto násobím. Odčítám pro to, aby kreslení začínalo v levém dolním rohu (pro 1,1 pixel 0,0)
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
            
        if Sour2_x < 1 or Sour2_x > mrizka_x or Sour2_x % 1 != 0 :      #Kontrola vstupu, prázdný vstup None je ošetřen samotnou fcí numinput
            Sour2_x = numinput(f"Tah {i} hráče {hrac2}","Chybná souřadnice x, zadej platnou:")
            
            continue
        else:
            break

    Sour2_y = numinput(f"Tah {i} hráče {hrac2}", f"{hrac2}, zvol souřadnici y svého tahu:")

    while True:
            
        if Sour2_y < 1 or Sour2_y > mrizka_x or Sour2_y % 1 != 0 :      #Kontrola vstupu, prázdný vstup None je ošetřen samotnou fcí numinput
            Sour2_y = numinput(f"Tah {i} hráče {hrac2}","Chybná souřadnice y, zadej platnou:")   
                
            continue
        else:
            break

# Úprava souřadnic tak, aby kolečko bylo vykresleno uvnitř zvoleného pole mřížky:
    x2 = Sour2_x * k - (k/2)    # Násobení k <- jedno pole má k pixelů. Minus (k/2) -> Dostane se doprostřed pole na x-ové ose
    y2 = Sour2_y * k - (0.9*k)  # Násobení k <- jedno pole má k pixelů. Minus (0,9k) -> Dostane se do spodní části pole na y-ové ose


    # kreslení kolečka na zadaných souřadnicích:
    penup()
    goto([x2,y2])
    pendown()
    pensize(2)
    color("red")
    circle(0.4*k,360)


print(f"Děkuji, že jste hráli Pišqworky od Pepy, {hrac1} a {hrac2}! Gratuluji vítězi.")