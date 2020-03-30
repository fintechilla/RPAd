from functools import * #reduce


class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Point({}, {})".format(self.x, self.y)

    def __add__(self, number):
        return Point(self.x + number.x, self.y + number.y)

    def __sub__(self, number):
        return Point(self.x - number.x, self.y - number.y)


def add_sub_results(points):
    # p = Point(0,0)
    points = [Point(*point) for point in points]
    points_s = points
    print("inside add_sub_results: points: {}".format(points))
    for p in points:
        print(p)

    for p in points_s:
        print(p)

    return map(str(reduce(lambda x, y: points.pop().__add__(points.pop()), points)),  #,
            str(reduce(lambda x, y: points_s.pop().__sub__(points_s.pop()), points_s)))


# points = [(2, 3), (4, 5)]

res = add_sub_results([(3, 5), (7, 9)])
print("res: {}".format(res))
