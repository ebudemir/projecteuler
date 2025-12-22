from cProfile import label

import numpy as np

from matplotlib import pyplot as plt


# ---------- H_{a,b}(x) ----------
def H(a, b, x):
    return 0.5 - (b * np.cos(a * np.pi * x) + a * np.cos(b * np.pi * x)) / (2 * (a + b))


# ---------- derivative of H_{a,b}(x) ----------
def d_H(a, b, x):
    return a * b * np.pi * (np.sin(a * np.pi * x) + np.sin(b * np.pi * x)) / (2 * (a + b))


# ---------- plot of H_{a,b}(x) ----------
def plot_H(a, b, n=1000):
    x = np.linspace(0, 1, n)
    y35 = H(3, 5, x)
    y37 = H(3,7, x)
    dy35 = d_H(3,5,x)
    dy37 = d_H(3,7,x)

    plt.figure()
    #plt.plot(x, y35, label="35")
    #plt.plot(x, y37, label="37")
    plt.plot(x, dy35, label="dy35")
    plt.plot(x, dy37, label="dy37")
    #plt.plot(x, dy37)
    plt.xlabel("x")
    plt.ylabel(r"$H_{a,b}(x)$")
    plt.title(f"H_{{{a},{b}}}(x)")
    plt.grid(True)
    plt.legend()
    plt.show()


# ---------- solve H_{a,b}(x) = H_{c,d}(y) for y ----------
def solve_y(a, b, c, d, x, tol=1e-12):
    target = H(a, b, x)
    lo, hi = 0.0, 1.0

    for _ in range(60):  # bisection
        mid = 0.5 * (lo + hi)
        if H(c, d, mid) < target:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


# ---------- solve H_{a,b}(x) = H_{c,d}(y) = z for (x,y,z) ----------
def solve_y(a, b, c, d):
    n = 10000
    zz = np.linspace(0, 1, n)
    xx = H(a, b, zz)
    yy = H(c, d, zz)
    x_points = []
    y_points = []
    z_points = []
    for z in zz:
        mn = xx - z
        indexes_x = np.where(((mn[:-1] <= 0) & (mn[1:] > 0)) | ((mn[:-1] >= 0) & (mn[1:] < 0)))[0]
        mn = yy - z
        indexes_y = np.where(((mn[:-1] <= 0) & (mn[1:] > 0)) | ((mn[:-1] >= 0) & (mn[1:] < 0)))[0]
        print(indexes_x, indexes_y, z)

        for x in indexes_x:
            for y in indexes_y:
                x_points.append(zz[x])
                y_points.append(zz[y])
                z_points.append(z)

    plt.figure()
    plt.scatter(x_points, y_points, s=1, c=z_points, cmap='viridis')
    plt.xlabel("x")
    plt.ylabel(r"$H_{a,b}(x)$")
    plt.title(f"H_{{{a},{b}}}(x)")
    plt.grid(True)
    plt.show()


# ---------- compute F(a,b,c,d) ----------
def F(a, b, c, d, N=20000):
    xs = np.linspace(0.0, 1.0, N)
    zs = np.empty(N)

    for i, x in enumerate(xs):
        zs[i] = H(a, b, x)

    # total variation = sum |delta z|
    return np.sum(np.abs(np.diff(zs)))


# ---------- primes ----------
def primes_between(m, n):
    sieve = np.ones(n + 1, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i:n + 1:i] = False
    return [i for i in range(m, n + 1) if sieve[i]]


# ---------- compute G(m,n) ----------
def G(m, n, N=20000):
    primes = primes_between(m, n)
    total = 0.0
    count = 0

    for i, p in enumerate(primes):
        for q in primes[i + 1:]:
            total += F(p, q, p, 2 * q - p, N=N)
            count += 1

    return total, count


# ---------- example tests ----------
if __name__ == "__main__":
    #print("F(3,5,3,7) ≈", F(3, 5, 3, 7))
    #print("F(7,17,9,19) ≈", F(7, 17, 9, 19))

    #val, cnt = G(3, 20, N=12000)
    #print("G(3,20) ≈", val, " over ", cnt, " pairs")
    #print(H(3, 5, 0))
    #plot_H(3, 5)
    solve_y(3,5, 3, 7)
