import sympy


def distinct_pf_count(n):
    return len(sympy.factorint(n))


consec = 4
n = 2
while True:
    if all(distinct_pf_count(n + i) == consec for i in range(consec)):
        print(n)
        break
    n += 1
