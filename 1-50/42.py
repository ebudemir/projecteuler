def word_value(word):
    return sum(ord(c) - ord('A') + 1 for c in word)

# Precompute triangle numbers up to the maximum possible word value
triangles = set()
n = 1
while True:
    t = n * (n + 1) // 2
    triangles.add(t)
    if t > 1000:  # more than enough for word values
        break
    n += 1

# Read and evaluate all words
count = 0
with open("0042_words.txt", "r") as f:
    words = f.read().replace('"', '').split(',')

for w in words:
    if word_value(w) in triangles:
        count += 1

print(count)
