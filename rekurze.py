U = 60

from turtle import exitonclick, forward, left, right, forward

def koch(uroven, D):
    
    if uroven > 1:
        forward(D)
        left(U)
        koch(uroven-1, D/3)
        

koch(10,250)