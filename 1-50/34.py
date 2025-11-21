import math


def sum_digit_factorials(n):
    return sum(math.factorial(int(d)) for d in str(n))


limit = 7 * math.factorial(9)  # 2540160
matches = [n for n in range(3, limit + 1) if n == sum_digit_factorials(n)]
print(matches)
print(sum(matches))
