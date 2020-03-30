from datetime import datetime as dt
from datetime import timedelta as td
from datetime import time as tm



# x = lambda a : a + 10
#
# print(x(5))

# import datetime as dt
print(td(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=11, weeks=0))
timeNow = dt.now()
print(timeNow.hour)
print(timeNow.weekday())
td1hr = td(hours=1)
print(td1hr)
if int(18) >= timeNow.hour >= int(13) and timeNow.weekday() <= 4:
    print("Correct - " + timeNow.strftime("%Y-%m-%d-%H:%M:%S"))
    print(timeNow.hour + 12)

else:
    print("too soon")

dfor1 = ""

print("not bool(dfor1){}, dfor1 == ' '{}, dfor1 is None{}".format(not bool(dfor1),
                                                                                           dfor1 == " ", dfor1 is None))
a = "a "
if len(a) == 1:
    print("ord(a): {}".format(ord(a)))

else:
    print("len not equal to 1")
