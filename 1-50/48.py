MOD = 10**10
total = sum(pow(i, i, MOD) for i in range(1, 1001)) % MOD
print(f"{total:010d}")  # print with leading zeros if any
