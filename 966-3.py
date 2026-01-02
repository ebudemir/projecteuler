import math

import numpy as np


def get_radius(a, b, c):
    area = math.sqrt((a + b + c) * (a + b - c) * (a - b + c) * (- a + b + c)) / 4
    return math.sqrt(area / math.pi)


def get_coordinates(a, b, c):
    Ax, Ay = 0, 0
    Bx, By = c, 0
    Cx = (c ** 2 - a ** 2 + b ** 2) / (2 * c)
    Cy = math.sqrt(b ** 2 - Cx ** 2)
    return Ax, Ay, Bx, By, Cx, Cy


if __name__ == "__main__":
    a, b, c = 30, 40, 60
    Ax, Ay, Bx, By, Cx, Cy = get_coordinates(a, b, c)
    r = get_radius(a, b, b)
    xmax = max(Ax, Bx, Cx)
    ymax = max(Ay, By, Cy)

    arr = np.full((int(xmax), int(ymax)), True, dtype=bool)
    x_ind, y_ind = np.indices(arr.shape)
    arr[Cx * y_ind - Cy * x_ind > 0] = False
    arr[(Cx - c) * y_ind - Cy * x_ind + Cy * c < 0] = False
    max_area = 0
    res = np.empty((int(xmax), int(ymax)), dtype=np.int64)
    for x in range(xmax):
        for y in range(int(ymax)):
            arr_copy = arr.copy()
            arr_copy[(x_ind - x) ** 2 + (y_ind - y) ** 2 > r ** 2] = False
            count = np.sum(arr_copy)
            res[x, y] = count
            if count > max_area:
                max_area = count
                print(x, y, max_area)
    np.save("966.npy", res)
