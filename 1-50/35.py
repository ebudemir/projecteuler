def sieve(limit):
    is_prime = [True] * limit
    is_prime[0:2] = [False, False]
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit, i):
                is_prime[j] = False
    primes = {i for i, val in enumerate(is_prime) if val}
    return primes


primes = sieve(1000000)


def rotations(n):
    s = str(n)
    return [int(s[i:] + s[:i]) for i in range(len(s))]


circular_primes = set()

for p in primes:
    if all(rot in primes for rot in rotations(p)):
        circular_primes.add(p)

print(len(circular_primes))
