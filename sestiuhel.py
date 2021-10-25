x = input("Zadejte x rozměr vaší mřížky:")
x = int(x)
y = input("Zadejte x rozměr vaší mřížky:")
y = int(y)

from turtle import forward,right,left,exitonclick,penup,pendown,speed
from math import sqrt
speed(0)

for _ in range(y):
    for _ in range(x):
        for _ in range(8):
            
            left(60)
            forward(16)

        penup()    
        
        right(120)
        pendown()

    penup()
    right(90)                           #funkční, vrátí se
    forward(x*(16*sqrt(3)))             #funkční, vrátí se, hodnota vypočtena přes cosinovu větu
    
    left(90)
    forward(16)
    left(120)
    forward(16)
    right(480)
    forward(16)
    
    pendown()

exitonclick()