

from sys import stdin
from collections import Counter
from itertools import combinations

def min_max_wins(n, a, b):
    cnt_a = Counter(a)
    cnt_b = Counter(b)
    w_a = 0
    w_b = 0
    for k, v in cnt_b.items():
        if k == "R":
            w_b += min(v, cnt_a["S"])
            w_a += min(v, cnt_a["P"])
        elif k == "S":
            w_b += min(v, cnt_a["P"])
            w_a += min(v, cnt_a["R"])
        elif k == "P":
            w_b += min(v, cnt_a["R"])
            w_a += min(v, cnt_a["S"])
    return w_a, w_a + n - w_b

def main():
    n = int(stdin.readline().strip())
    a = stdin.readline().strip().split(" ")
    b = stdin.readline().strip().split(" ")
    print(" ".join(map(str, min_max_wins(n, a, b))))

if __name__ == "__main__":
    main()
