import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

count = 0
num = 1
while count < 10001:
    num += 1
    if is_prime(num):
        count += 1

print(num)
