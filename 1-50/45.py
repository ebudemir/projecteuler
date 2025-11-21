import math


def is_pentagonal(x):
    t = (1 + math.sqrt(1 + 24 * x)) / 6.0
    return t.is_integer()


# start after the known solution H_143 = 40755
n = 144
while True:
    h = n * (2 * n - 1)
    if is_pentagonal(h):
        print(h)  # 1533776805
        break
    n += 1
