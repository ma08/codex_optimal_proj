
from sys import stdin
from collections import defaultdict
from itertools import permutations

def min_max_wins(n, a, b):
    cnt_a = defaultdict(int)
    cnt_b = defaultdict(int)
    for i in a:
        cnt_a[i] += 1
    for i in b:
        cnt_b[i] += 1
    w_a = 0
    w_b = 0
    w_a += min(cnt_a["R"], cnt_b["S"])
    w_a += min(cnt_a["S"], cnt_b["P"])
    w_a += min(cnt_a["P"], cnt_b["R"])
    w_b += min(cnt_b["R"], cnt_a["S"])
    w_b += min(cnt_b["S"], cnt_a["P"])
    w_b += min(cnt_b["P"], cnt_a["R"])
    return w_a, w_b

def main():
    n = int(stdin.readline().strip())
    a = stdin.readline().strip().split(" ")
    b = stdin.readline().strip().split(" ")
    print(" ".join(map(str, min_max_wins(n, a, b))))

if __name__ == "__main__":
    main()
