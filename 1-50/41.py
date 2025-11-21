import itertools
import sympy


def largest_pandigital_prime():
    # Try 7-digit pandigitals first, then 4-digit (the next possible)
    for n in range(7, 0, -1):
        digits = ''.join(str(i) for i in range(1, n + 1))
        # Permute in descending order for early exit
        for p in sorted(itertools.permutations(digits), reverse=True):
            num = int(''.join(p))
            if sympy.isprime(num):
                return num


print(largest_pandigital_prime())
