# Read the file
with open("0022_names.txt") as f:
    names = f.read()

# Remove quotes and split by comma
names = names.replace('"', '').split(',')

# Sort alphabetically
names.sort()


def name_value(name):
    return sum(ord(c) - ord('A') + 1 for c in name)


total_score = sum((i + 1) * name_value(name) for i, name in enumerate(names))
print(total_score)
