def sum_even_fib(limit=4_000_000):
    a, b = 1, 2  # Fibonacci starts with 1, 2
    total = 0

    while b <= limit:
        if b % 2 == 0:
            total += b
        a, b = b, a + b

    return total


if __name__ == "__main__":
    print(sum_even_fib())
