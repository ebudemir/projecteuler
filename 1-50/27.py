import sympy


def consecutive_primes_count(a, b):
    n = 0
    while True:
        value = n ** 2 + a * n + b
        if value < 2 or not sympy.isprime(value):
            return n
        n += 1


max_count = 0
product = 0

# b must be prime (positive or negative)
primes_b = list(sympy.primerange(2, 1000))

for a in range(-999, 1000):
    for b in primes_b:
        # try positive b
        count = consecutive_primes_count(a, b)
        if count > max_count:
            max_count = count
            product = a * b
        # try negative b
        count = consecutive_primes_count(a, -b)
        if count > max_count:
            max_count = count
            product = a * (-b)

print(product)
