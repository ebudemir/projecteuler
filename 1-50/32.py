def is_1_to_9_pandigital(s):
    return len(s) == 9 and set(s) == set('123456789')

products = set()

# Case 1: 1-digit * 4-digit = 4-digit
for a in range(1, 10):               # 1-digit a
    for b in range(1000, 10000):     # 4-digit b
        prod = a * b
        s = f"{a}{b}{prod}"
        if is_1_to_9_pandigital(s):
            print(a, "x", b, "=", prod)
            products.add(prod)

# Case 2: 2-digit * 3-digit = 4-digit
for a in range(10, 100):             # 2-digit a
    for b in range(100, 1000):       # 3-digit b
        prod = a * b
        s = f"{a}{b}{prod}"
        if is_1_to_9_pandigital(s):
            print(a, "x", b, "=", prod)
            products.add(prod)

result = sum(products)
print(result)   # 45228
