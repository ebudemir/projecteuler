import numpy as np
from matplotlib import pyplot as plt


# ---------- H_{a,b}(x) ----------
def H(a, b, x):
    return 0.5 - (b * np.cos(a * np.pi * x) + a * np.cos(b * np.pi * x)) / (2 * (a + b))


def d_H(a, b, x):
    return a * b * np.pi * (np.sin(a * np.pi * x) + np.sin(b * np.pi * x)) / (2 * (a + b))


def find_roots_on_grid(fvals, grid, z):
    diff = fvals - z
    idx = np.where(diff[:-1] * diff[1:] <= 0)[0]
    return grid[idx]


def solve_xyz(a, b, c, d, n=5000):
    grid = np.linspace(0, 1, n)
    Hx = H(a, b, grid)
    Hy = H(c, d, grid)

    X, Y, Z = [], [], []

    for z in np.linspace(0, 1, n):
        xs = find_roots_on_grid(Hx, grid, z)
        ys = find_roots_on_grid(Hy, grid, z)

        for x in xs:
            for y in ys:
                X.append(x)
                Y.append(y)
                Z.append(z)

    return np.array(X), np.array(Y), np.array(Z)


if __name__ == "__main__":
    primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    for p in primes:
        for q in primes:
            if q > p:
                r = 2 * q - p
                x, y, z = solve_xyz(p, q, p, r)
                plt.figure()
                # plt.xlim(0, 0.2)
                # plt.ylim(0, 0.3)
                plt.scatter(x, y, s=0.1, c=z, cmap='RdYlGn_r')
                xl = "$H_{" + str(p) + "," + str(q) + "}(x)$"
                plt.xlabel(xl)
                yl = "$H_{" + str(p) + "," + str(r) + "}(x)$"
                plt.ylabel(yl)
                plt.grid(True)
                #plt.show()
                filename = "p_" + str(p) + "_" + str(q) + "-" + str(p) + "_" + str(r) + ".png"
                plt.savefig(filename)
                print(filename)
                plt.close("all")

