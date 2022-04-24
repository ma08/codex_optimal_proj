

from sys import stdin
from collections import Counter

def min_max_wins(n, a_cnt, b_cnt):
    w_a = sum(min(a_cnt[k], b_cnt[k]) for k in "RSP".split())
    w_b = sum(min(a_cnt[k], b_cnt["RSP".replace(k, "")]) for k in "RSP".split())
    return w_a, w_b

def main():
    n = int(stdin.readline().strip())
    a_cnt = Counter(stdin.readline().strip().split(" "))
    b_cnt = Counter(stdin.readline().strip().split(" "))
    print(" ".join(map(str, min_max_wins(n, a_cnt, b_cnt))))

if __name__ == "__main__":
    main()
