import math


def sieve(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0:2] = [False, False]
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return is_prime


LIMIT = 10000
is_prime = sieve(LIMIT)
primes = [i for i, p in enumerate(is_prime) if p]


def is_sum_of_prime_and_twice_square(n):
    for p in primes:
        if p >= n:
            break
        rem = n - p
        if rem % 2 != 0:
            continue
        k2 = rem // 2
        k = int(math.isqrt(k2))
        if k * k == k2:
            return True
    return False


for n in range(3, LIMIT, 2):  # odd numbers
    if is_prime[n]:
        continue  # skip primes
    if not is_sum_of_prime_and_twice_square(n):
        print(n)
        break
