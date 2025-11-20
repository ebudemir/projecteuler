def proper_divisor_sum(n):
    total = 1  # 1 is always a proper divisor
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
    return total


# Step 1: List abundant numbers
abundant = [i for i in range(12, 28124) if proper_divisor_sum(i) > i]

# Step 2: Create a set of numbers that can be written as sum of two abundant numbers
can_be_written = set()
for i in abundant:
    for j in abundant:
        s = i + j
        if s <= 28123:
            can_be_written.add(s)

# Step 3: Sum all numbers that cannot be written as sum of two abundant numbers
total = sum(n for n in range(1, 28124) if n not in can_be_written)
print(total)
