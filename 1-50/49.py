import itertools
from sympy import isprime

# Generate all 4-digit primes
primes = [p for p in range(1000, 10000) if isprime(p)]

# Store sequences found
sequences = []

for p in primes:
    # get all permutations of p's digits
    perms = set(int(''.join(t)) for t in itertools.permutations(str(p)))
    # filter to 4-digit primes
    prime_perms = sorted([x for x in perms if x in primes and x >= 1000])

    # check all combinations of 3 numbers
    for i in range(len(prime_perms)):
        for j in range(i+1, len(prime_perms)):
            for k in range(j+1, len(prime_perms)):
                a, b, c = prime_perms[i], prime_perms[j], prime_perms[k]
                if b - a == c - b:
                    seq = (a, b, c)
                    # avoid the known sequence 1487,4817,8147
                    if seq != (1487, 4817, 8147):
                        sequences.append(seq)

# Print the concatenated 12-digit number(s)
for seq in sequences:
    print('Sequence:', seq, 'Concatenated:', ''.join(map(str, seq)))
