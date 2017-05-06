class shape:

    def draw(self):
        print ("draw")

    def area(self):
        print ("area")

class Rectangle(shape):

    def __init__(self):
        self.length= 0
        self.width= 0
    def draw(self):
        print ("draw")

    def area(self):
        print ("area")

class Triangle (shape):
    def __init__(self):
        self.a=0
        self.b=0
        self.c=0
    def draw(self):
        print ("draw")

    def area(self):
        print ("area")

@staticmethod
def printType():
    print("Print Type")

s= shape()
r = Rectangle()
t= Triangle()

s.area()
s.draw()

r.area()
r.draw()

t.area()
t.draw()
