
import itertools

def solve(n, m, s, d, c):
    if n < m:
        return "impossible"
    n_slots = list(itertools.combinations(range(s), m))  # combinations of slots to change
    n_new = list(itertools.combinations(range(n), m))  # combinations of new files
    max_p = 0
    max_p_scheme = []  # the scheme with the highest probability
    for slots in n_slots:
        for new in n_new:
            p = 1  # probability
            for i in range(m):
                p *= (c[slots[i]] + new[i]) / d
            if p > max_p:
                max_p = p
                max_p_scheme = [0]*s  # reset
                for i in range(m):
                    max_p_scheme[slots[i]] += new[i]
    return " ".join(map(str, max_p_scheme))

def main():
    n, m, s, d = map(int, input().split(" "))
    c = list(map(int, input().split(" ")))
    print(solve(n, m, s, d, c))

if __name__ == "__main__":
    main()
