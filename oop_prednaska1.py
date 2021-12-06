class Point:
    counter = 0

    def __init__(self, x=0, y=0):           # __ znamená private, _ by znamenalo protected
        self.__id = Point.counter
        self.__x = x
        self.__y = y
        Point.counter += 1

    def print(self):
        print(self.__id, self.__x, self.__y)

    def getAmountOfObjects():
        return(Point.counter)

#Vytvoření objektu
p1 = Point(10,15)
print(Point.getAmountOfObjects())
p2 = Point(20,25)
print(Point.getAmountOfObjects())

p1.__x = 88

p1.print()
p2.print()