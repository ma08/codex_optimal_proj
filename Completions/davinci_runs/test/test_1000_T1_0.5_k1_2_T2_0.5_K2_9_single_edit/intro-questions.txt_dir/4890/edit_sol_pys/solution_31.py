
import itertools

def solve(n, m, s, d, c):
    if n < m:
        return "impossible"
    n_slots = list(itertools.combinations(range(s), m)) # n_slots[0] = (0, 1, 2)
    n_new = list(itertools.combinations(range(n), m)) # n_new[0] = (0, 1, 2)
    max_p = 0
    max_p_scheme = []
    for slots in n_slots:
        for new in n_new:
            p = 1
            for i in range(m):
                p *= (c[slots[i]] + new[i]) / d
            if p > max_p:
                max_p = p
                max_p_scheme = [0]*s # [0, 0, 0, 0, 0]
                for i in range(m):
                    max_p_scheme[slots[i]] += new[i]
    return " ".join(map(str, max_p_scheme)) # "1 2 3 4 5"

def main():
    n, m, s, d = map(int, input().split(" "))
    c = list(map(int, input().split(" ")))
    print(solve(n, m, s, d, c))

if __name__ == "__main__":
    main()
