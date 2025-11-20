def is_palindrome(n):
    return str(n) == str(n)[::-1]


max_palindrome = 0

for i in range(999, 99, -1):
    for j in range(i, 99, -1):  # j <= i to avoid repeats
        p = i * j
        if is_palindrome(p):
            print(i, j, p)
            if p > max_palindrome:
                max_palindrome = p

print(max_palindrome)
