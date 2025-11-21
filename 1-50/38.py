def is_1_to_9_pandigital(s):
    return len(s) == 9 and set(s) == set('123456789')


max_pandigital = 0

for i in range(1, 10000):
    concat = ''
    n = 1
    while len(concat) < 9:
        concat += str(i * n)
        n += 1
    if is_1_to_9_pandigital(concat):
        max_pandigital = max(max_pandigital, int(concat))

print(max_pandigital)
