from math import comb, factorial
import math
from decimal import Decimal, getcontext

getcontext().prec = 100


def P_A_intersect_B_closed(n, k):
    if n < 1:
        raise ValueError("n>=1 required")
    if k <= 0:
        return 0.0
    # r = floor(k)
    r = math.floor(k)
    # max index to check is min(n, r) (if k integer, U_r may be zero)
    max_i = min(n, r)
    total = 0.0
    for i in range(0, max_i + 1):
        U = max(0.0, k - i)
        V = max(0.0, k - 1 - i)
        term = (U ** (n + 1) - V ** (n + 1)) / (n + 1) + (i - (k - 1)) * (U ** n - V ** n) / n
        total += ((-1) ** i) * comb(n, i) * term
    return total / factorial(n - 1)


def factorial_decimal(n):
    """Compute n! using Decimal, without math.factorial."""
    result = Decimal(1)
    for i in range(2, n + 1):
        result *= Decimal(i)
    return result


def comb_decimal(n, k):
    """Compute nCk using integer arithmetic (no math.comb)."""
    if k < 0 or k > n:
        return Decimal(0)
    k = min(k, n - k)  # symmetry
    numerator = Decimal(1)
    denominator = Decimal(1)
    for i in range(k):
        ii = Decimal(i)
        numerator *= (n - ii)
        denominator *= (ii + 1)
    return numerator / denominator


def P_A_intersect_B_closed_decimal(n, k):
    if n < 1:
        raise ValueError("n>=1 required")
    if k <= 0:
        return 0.0
    # r = floor(k)
    r = math.floor(k)
    # max index to check is min(n, r) (if k integer, U_r may be zero)
    nn = Decimal(n)
    rr = Decimal(r)
    kk = Decimal(k)
    max_i = min(n, r)
    total = Decimal(0)
    for i in range(0, max_i + 1):
        ii = Decimal(i)
        U = max(Decimal(0), kk - ii)
        V = max(Decimal(0), kk - 1 - ii)
        term = (U ** (nn + 1) - V ** (nn + 1)) / (nn + 1) + (ii - (kk - 1)) * (U ** nn - V ** nn) / nn
        total += (Decimal(-1) ** i) * comb_decimal(n, i) * term
    return total / factorial_decimal(n - 1)


def go(k):
    print("*****************************************************")
    print("***********************", k, "***********************")
    print("*****************************************************")
    getcontext().prec = 1000000
    # Increase precision and max exponent
    getcontext().Emax = 9999999     # maximum exponent
    getcontext().Emin = -9999999   # minimum exponent
    expected = 0
    total = 0
    for i in range(999000, 7 * k):
        val = P_A_intersect_B_closed_decimal(i, k)
        ex = (i + 1) * val
        expected += ex
        # print(i+1, k, val, expected)
        print(i + 1, expected)


if __name__ == "__main__":
    for i in range(1000000, 1000001):
        go(i)
