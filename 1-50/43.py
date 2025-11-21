import itertools

divs = [2,3,5,7,11,13,17]

total = 0
digits = '0123456789'

# We build permutations but prune early: check each 3-digit window as soon as it's available.
for perm in itertools.permutations(digits):
    # d2d3d4 must be divisible by 2 -> d4 even (perm indices 1..3 -> check perm[3])
    if int(perm[3]) % 2 != 0:
        continue
    # d4d5d6 (indices 3..5) divisible by 5 -> last digit 0 or 5
    if perm[5] not in '05':
        continue

    ok = True
    # Check remaining 3-digit divisibility constraints
    for i, p in enumerate(divs):  # p corresponds to divisibility of d_{i+2}d_{i+3}d_{i+4}
        tri = int(''.join(perm[i+1:i+4]))
        if tri % p != 0:
            ok = False
            break
    if ok:
        total += int(''.join(perm))

print(total)  # 16695334890
