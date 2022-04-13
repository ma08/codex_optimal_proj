
import itertools

def solve(n, m, s, d, c):
    if n < m:
        return "impossible"
    n_slots = list(itertools.combinations(range(s), m)) # n_slots is the number of slot combinations (1)
    n_new = list(itertools.combinations(range(n), m)) # n_new is the number of new combinations (2)
    max_p = 0
    max_p_scheme = [] # max_p_scheme is a scheme with the highest probability
    for slots in n_slots:
        for new in n_new:
            p = 1 # p is the probability of a scheme
            for i in range(m):
                p *= (c[slots[i]] + new[i]) / d
            if p > max_p:
                max_p = p # update the highest probability
                max_p_scheme = [0]*s # update the scheme
                for i in range(m):
                    max_p_scheme[slots[i]] += new[i]
    return " ".join(map(str, max_p_scheme))

def main():
    n, m, s, d = map(int, input().split(" "))
    c = list(map(int, input().split(" ")))
    print(solve(n, m, s, d, c))

if __name__ == "__main__":
    main()
