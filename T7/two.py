from abc import ABC, abstractmethod

"""I have created the shape class as an abstract clsas becuase i felt there's no need to create an instance of the class.
additionally, the area functin of the shape class can be implemented accordingly by the child class"""


class Shape(ABC):
    def __init__(self):
        self.default_area = 0

    @abstractmethod
    def area(self):
        pass


class Square(Shape):
    def __init__(self, l):
        super().__init__()
        self.length = l

    def area(self):
        self.default_area = self.length * self.length
        return self.default_area


s1 = Square(9)
print(s1.default_area)
print(s1.area())
