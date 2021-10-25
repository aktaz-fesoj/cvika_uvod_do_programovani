x = input("Zadejte x rozměr vaší mřížky:")
x = int(x)
y = input("Zadejte x rozměr vaší mřížky:")
y = int(y)

from turtle import forward,right,left,exitonclick,penup,pendown,speed

speed(7)

for _ in range(y):
    for _ in range(x):
        for _ in range(4):
            forward(25)
            left(90)
        forward(25)

    penup()
    left(180)
    forward(25*x)
    left(90)
    forward(25)
    left(90)
    pendown()
    

exitonclick()




