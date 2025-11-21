def fifth_sum(n):
    return sum(int(d) ** 5 for d in str(n))


limit = 6 * 9 ** 5  # 354294
matches = [n for n in range(2, limit + 1) if fifth_sum(n) == n]
print(matches)
print(sum(matches))
