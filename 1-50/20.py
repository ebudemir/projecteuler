import math

n = math.factorial(100)
digit_sum = sum(int(d) for d in str(n))
print(digit_sum)   # Expected: 648
