import math

# Digits to permute
digits = list(range(10))

# Target permutation (1 millionth)
target = 1_000_000 - 1  # zero-indexed

permutation = []

# Number of digits
n = len(digits)

for i in range(n, 0, -1):
    fact = math.factorial(i - 1)
    index = target // fact
    permutation.append(digits.pop(index))
    target %= fact

# Convert to string
result = ''.join(map(str, permutation))
print(result)
