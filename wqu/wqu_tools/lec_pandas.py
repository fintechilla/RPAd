import pandas as pd

df = pd.DataFrame({'a': [1, 2, 5], 'b': [True, False, True]})
print(type(df))
print(df.head())


class Rectangle(object):
    def __init__(self, height, length):
        self.height = height
        self.length = length

    def area(self):
        return self.height * self.length

    def perimeter(self):
        return 2 * (self.height + self.length)


print("Rectangle")

class Square(Rectangle):
    def __init__(self, length):
        super(Square, self).__init__(length, length)

print("Square")

s = Square(5)
print(("area s  : {}; perimeter: {}".format(s.area(), s.perimeter())))
rec = Rectangle(5, 5)
print(("area rec: {}; perimeter: {}".format(rec.area(), rec.perimeter())))
print("type of Square {}".format(type(s)))
print("type of Rec {}".format(type(rec)))

print("isInstance: {}".format(isinstance(s, Rectangle)))