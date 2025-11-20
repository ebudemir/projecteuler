limit = 1_000_000
collatz_cache = {1: 1}


def collatz_length(n):
    if n in collatz_cache:
        return collatz_cache[n]
    if n % 2 == 0:
        next_n = n // 2
    else:
        next_n = 3 * n + 1
    length = 1 + collatz_length(next_n)
    collatz_cache[n] = length
    return length


max_length = 0
starting_number = 0

for i in range(1, limit):
    length = collatz_length(i)
    if length > max_length:
        max_length = length
        starting_number = i

print(starting_number)
