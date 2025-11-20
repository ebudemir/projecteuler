import math


def num_divisors(n):
    count = 1
    i = 2
    while i * i <= n:
        exp = 0
        while n % i == 0:
            n //= i
            exp += 1
        count *= (exp + 1)
        i += 1
    if n > 1:
        count *= 2
    return count


n = 1
while True:
    if n % 2 == 0:
        divisors = num_divisors(n // 2) * num_divisors(n + 1)
    else:
        divisors = num_divisors(n) * num_divisors((n + 1) // 2)
    if divisors > 500:
        print(n * (n + 1) // 2)
        break
    n += 1
