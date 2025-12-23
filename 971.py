import sys
import threading


def main():
    import math

    # ------------------------------------------------------------
    # Generate all primes up to N using a fast sieve
    # ------------------------------------------------------------
    def primes_up_to(n):
        sieve = bytearray(b"\x01") * (n + 1)
        sieve[0:2] = b"\x00\x00"
        import math
        r = int(math.isqrt(n))
        for i in range(2, r + 1):
            if sieve[i]:
                step = i
                start = i * i
                sieve[start:n + 1:step] = b"\x00" * (((n - start) // step) + 1)
        return [i for i in range(n + 1) if sieve[i]]

    # ------------------------------------------------------------
    # Compute m_p for a given prime p ≡ 1 (mod 5)
    # Using the reduced dynamical system on the 5th roots of unity.
    # ------------------------------------------------------------
    def compute_mp(p):
        # t = (p-1)/5
        t = (p - 1) // 5

        # The 5th roots of unity correspond to integers 0..4 representing ω^j

        # We need a primitive 5th root of unity in F_p.
        # Find g a primitive root, then ζ = g^t gives a 5th root of unity.
        # Represent ω^j simply as j.
        # Compute the map j -> new_j where ω ↦ ω(ω+1)^t.

        # Find primitive root mod p
        def primitive_root(p):
            # factor p-1
            phi = p - 1
            fac = []
            n = phi
            d = 2
            while d * d <= n:
                if n % d == 0:
                    fac.append(d)
                    while n % d == 0:
                        n //= d
                d += 1
            if n > 1: fac.append(n)
            for g in range(2, p):
                ok = True
                for q in fac:
                    if pow(g, phi // q, p) == 1:
                        ok = False
                        break
                if ok:
                    return g
            return None

        g = primitive_root(p)
        zeta = pow(g, t, p)  # ζ = g^t

        # Precompute ζ^j for j in [0..4]
        zeta_pow = [pow(zeta, j, p) for j in range(5)]

        # Build map on {0,1,2,3,4}
        nxt = [0] * 5
        for j in range(5):
            w = zeta_pow[j]
            v = (w + 1) % p  # (ω + 1)
            w_new = (w * pow(v, t, p)) % p
            # Find which j' satisfies ζ^j' = w_new
            # Since group is small, we just check
            for jp in range(5):
                if zeta_pow[jp] == w_new:
                    nxt[j] = jp
                    break

        # Find cycles and count cycle nodes that are not j corresponding to ω = -1
        # Determine which j gives ω=-1
        minus1_j = None
        for j in range(5):
            if zeta_pow[j] == p - 1:
                minus1_j = j
                break

        visited = [0] * 5
        mp = 0

        for start in range(5):
            if visited[start]: continue
            # Explore the component
            path = {}
            cur = start
            step = 0
            while not visited[cur]:
                visited[cur] = 1
                path[cur] = step
                step += 1
                cur = nxt[cur]
            # 'cur' is now in a cycle
            cycle_start = cur
            cycle_length = 1
            cur = nxt[cur]
            while cur != cycle_start:
                cycle_length += 1
                cur = nxt[cur]

            # Collect cycle nodes
            cycle_nodes = []
            cur = cycle_start
            cycle_nodes.append(cur)
            cur = nxt[cur]
            while cur != cycle_start:
                cycle_nodes.append(cur)
                cur = nxt[cur]

            # If cycle contains -1, ignore it
            if minus1_j in cycle_nodes:
                continue

            mp += len(cycle_nodes)

        return mp

    # ------------------------------------------------------------
    # Main computation
    # ------------------------------------------------------------

    N = 10 ** 8
    primes = primes_up_to(N)

    total = 0

    for p in primes:
        if p % 5 != 1:
            continue

        mp = compute_mp(p)
        c = 1 + mp * ((p - 1) // 5)
        print(p, c)
        total += c

    print(total)


if __name__ == "__main__":
    threading.Thread(target=main).start()
