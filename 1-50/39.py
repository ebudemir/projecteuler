max_solutions = 0
best_p = 0

for p in range(1, 1001):
    count = 0
    for a in range(1, p//3 + 1):
        for b in range(a, (p - a)//2 + 1):
            c = p - a - b
            if a*a + b*b == c*c:
                count += 1
    if count > max_solutions:
        max_solutions = count
        best_p = p

print(best_p)
