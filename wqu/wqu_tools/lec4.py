# import this
from lackey import *

from functools import reduce

add = lambda a: a + 10
open = lambda: type("n", KeyModifier.CTRL)
close = lambda: type("w", KeyModifier.CTRL)

print("Here: {} ".format(add(2)))
wait(3)


def do_sth(fn):
    print("inside do_sth()")
    fn()
    print("inside A/do_sth()")


do_sth(open)
wait(2)
do_sth(close)


# open()


def my_func(z, n):
    print("Hello: {} ".format(z(n)))


my_func(add, 6)


def some_decorator(f):
    def wraps(*args):
        print(f"Calling function '{f.__name__}'")
        return f(args)

    return wraps


@some_decorator
def decorated_function(x):
    print(f"With argument '{x}'")


decorated_function("Python")


# Defining a decorator
def trace(f):
    def wrap(*args, **kwargs):
        print(f"[TRACE] func: {f.__name__}, args: {args}, kwargs: {kwargs}")
        return f(*args, **kwargs)

    return wrap


# Applying decorator to a function
@trace
def add_two(x):
    return x + 2


# Calling the decorated function
add_two(3)

# Applying decorator to a lambda
print((trace(lambda x: x ** 2))(3))

iter = lambda *n: print(n)

iter(5, 4, 3)


def some_exponent(exponent):
    def func(x):
        return x ** exponent

    return func


print(some_exponent(2)(3), some_exponent(4)(2))


def print_todo_args(*args):
    print('I need to:')
    for arg in args:
        print('  ' + arg)


print_todo_args('watch_tv', 'read', 'eat', 'sleep')


class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Point({}, {})".format(self.x, self.y)


points = [(2, 3), (4, 5)]
points = [Point(*point) for point in points]
print("points class: {}".format(points.__class__))

print("points: {}, class of points: {}".format(points, points.__class__))


def add_sub_results(points):
    # points = [Point(*point) for point in points]
    print("inside add_sub...")
    return [str(reduce(lambda x, y: Point(x) + Point(y), points)),
            str(reduce(lambda x, y: Point(x) - Point(y), points))]


res = add_sub_results([(3, 5), (7, 9)])
# print("res: {}".format(res))

