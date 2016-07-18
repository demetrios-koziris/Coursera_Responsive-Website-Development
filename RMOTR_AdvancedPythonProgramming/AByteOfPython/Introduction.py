from functools import reduce

from datetime import datetime

def add1(*args):
    return reduce(lambda x, y: x-y, args)
print(add1(10,2, 3, 4))



add2 = lambda *args: args[0] + args[1]


print(str(datetime.now()))