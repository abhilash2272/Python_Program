from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        print(f"Area of rectangle is {self.l*self.b}")
class Circle(Shape):
    def __init__(self,r):
        self.r=r
    def area(self):
        print(f"radius of circle is {self.r*self.r*3.14}")
r=Rectangle(3,4)
r.area()
c=Circle(7)
c.area()

