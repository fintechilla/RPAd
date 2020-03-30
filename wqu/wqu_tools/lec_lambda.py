from functools import reduce


def fahrenheit(T):
    return (9 / 5) * T + 32


cels = (10, 20, 33.5)

fahr = map(fahrenheit, cels)
for f in fahr:
    print("fahr: {}".format(fahr))

Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = map(lambda x: (float(9) / 5) * x + 32, Celsius)
for f in Fahrenheit:
    print("print map (Fahrenheit): {}".format(f))

print("reduce: {}".format(reduce(lambda x, y, *z: x + y, [47, 11, 42, 13, -1])))

f = lambda a, b: a if (a > b) else b
print(reduce(f, [47, 11, 42, 102, 13]))
print(filter(f, [47, 11, 42, 102, 13]))

print(reduce(lambda x, y: x + y, range(1, 101)))
