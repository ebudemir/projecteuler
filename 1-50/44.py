def pent(n):
    return n * (3 * n - 1) // 2


# generate pentagonals and a set for fast membership
N = 10000  # large enough to find solution; 10000 works quickly
pent_list = [pent(i) for i in range(1, N + 1)]
pent_set = set(pent_list)

best_D = None

for k in range(2, N):
    Pk = pent_list[k - 1]
    # check j from k-1 downwards to try small differences first
    for j in range(k - 1, 0, -1):
        Pj = pent_list[j - 1]
        s = Pk + Pj
        d = Pk - Pj
        if s in pent_set and d in pent_set:
            best_D = d
            print("Found:", j, k, "Pj:", Pj, "Pk:", Pk, "D:", d)
            raise SystemExit

# If not found within N, increase N and retry
