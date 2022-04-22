

from sys import stdin
from collections import Counter
from itertools import combinations

def min_max_wins(n, A, B):
    cnt_A = Counter(A)
    cnt_B = Counter(B)
    w_a = 0
    w_b = 0
    for k, v in cnt_A.items():
        if k == "R":
            w_a += min(v, cnt_B["S"])
            w_b += min(v, cnt_B["P"])
        elif k == "S":
            w_a += min(v, cnt_B["P"])
            w_b += min(v, cnt_B["R"])
        elif k == "P":
            w_a += min(v, cnt_B["R"])
            w_b += min(v, cnt_B["S"])
    return w_a, w_b

def main():
    n = int(stdin.readline().strip())
    a = stdin.readline().strip().split(" ")
    b = stdin.readline().strip().split(" ")
    print(" ".join(map(str, min_max_wins(n, a, b))))

if __name__ == "__main__":
    main()
