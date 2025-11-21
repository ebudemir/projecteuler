import sympy

# Generate all primes below one million
primes = list(sympy.primerange(2, 10**6))
prime_set = set(primes)

max_len = 0
max_prime = 0

# Try sequences starting from each index
for start in range(len(primes)):
    total = 0
    for end in range(start, len(primes)):
        total += primes[end]
        if total >= 10**6:
            break
        if total in prime_set:
            length = end - start + 1
            if length > max_len:
                max_len = length
                max_prime = total

print(max_prime)  # 997651
