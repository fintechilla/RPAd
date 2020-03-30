

rootCause = "Password Reset - Manual"

data = rootCause.split("-")
print("data: {}; len {}; class {}".format(data, len(data), data.__class__))
for d in data:
    print("class od d: {}".format(d.__class__))
    print("B/d:{}; len(d): {}".format(d, len(d)))
    d = d.lstrip()
    print("d:{}; len(d): {}".format(d, len(d)))

print("  Manual".split())

