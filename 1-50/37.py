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


def is_truncatable_prime(p, prime_set):
    s = str(p)
    # exclude single-digit primes
    if len(s) == 1:
        return False
    # truncate left to right
    for i in range(len(s)):
        if int(s[i:]) not in prime_set:
            return False
    # truncate right to left
    for i in range(len(s), 0, -1):
        if int(s[:i]) not in prime_set:
            return False
    return True


truncatable_primes = [p for p in primes if is_truncatable_prime(p, primes)]
print(truncatable_primes)
print(sum(truncatable_primes))
