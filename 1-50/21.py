def d(n):
    """Return sum of proper divisors of n."""
    s = 1
    p = 2
    while p * p <= n:
        if n % p == 0:
            s += p
            if p * p != n:
                s += n // p
        p += 1
    return s if n > 1 else 0


amicable_sum = 0

for a in range(1, 10000):
    b = d(a)
    if b != a and b < 10000 and d(b) == a:
        print(a, b)
        amicable_sum += a

print(amicable_sum)  # Expected: 31626
