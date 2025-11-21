coins = [1, 2, 5, 10, 20, 50, 100, 200]
target = 200

ways = [0] * (target + 1)
ways[0] = 1  # one way to make 0: use no coins

for coin in coins:
    for amt in range(coin, target + 1):
        ways[amt] += ways[amt - coin]

print(ways[target])
