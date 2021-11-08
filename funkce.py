def ObsahKruhu(polomer):
    from math import pi
    obsah_kruhu = pi * polomer * polomer
    return(obsah_kruhu)


ooo = ObsahKruhu(float(input("Zadej poloměr kruhu:")))

print(ooo)