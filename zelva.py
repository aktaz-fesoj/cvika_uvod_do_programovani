from turtle import forward,right,left,exitonclick,penup,pendown,speed

penup()
speed(10)
left(180)
forward(300)
left(180)
pendown()
speed(4)

#čtverec:
for _ in range(4):         #_ se běžně používá jako iterační proměnná pokud ji nebudeme chtít později.
    forward(150)
    left(90)


#přesun:
penup()
forward(600)
pendown()

#šestiúhelník:
for _ in range(6):

    for _ in range(7):
        forward(90)
        left(60)
    left(240)




exitonclick()