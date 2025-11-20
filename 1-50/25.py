# Initialize first two Fibonacci numbers
a, b = 1, 1
index = 2  # F1 = 1, F2 = 1

# Loop until we find a Fibonacci number with 1000 digits
while True:
    a, b = b, a + b
    index += 1
    if len(str(b)) >= 1000:
        break

print(index)
