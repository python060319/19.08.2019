class Shape:
    def __init__(self, name):
        self.name = name

class FourSides(Shape):
    def __init__(self, name,
                 a, b, c, d):
        super().__init__(name)
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    def __str__(self):
        return self.__str__() +\
               f'{a} {b} {c} {d} Hekef: {self.getHekef()}'
    def getHekef(self):
        return a + b + c + d

class Rectangle(FourSides):
    def __init__(self, name, a, b):
        super.__init__(name, a, b, a, b)
    def getHekef(self):
        return self.a * 2 + self.b * 2

