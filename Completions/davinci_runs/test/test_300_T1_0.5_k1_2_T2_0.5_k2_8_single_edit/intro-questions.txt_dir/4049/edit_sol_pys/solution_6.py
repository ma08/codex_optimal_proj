
from sys import stdin
from collections import defaultdict

def min_max_wins(n, a, b):
    cnt_a = defaultdict(int)
    cnt_b = defaultdict(int)
    for x in a:
        cnt_a[x] += 1
    for x in b:
        cnt_b[x] += 1
    w_a = 0
    w_b = 0
    for k, v in cnt_a.items():
        if k == "R":
            w_a += min(v, cnt_b["S"])
            w_b += min(v, cnt_b["P"])
        elif k == "S":
            w_a += min(v, cnt_b["P"])
            w_b += min(v, cnt_b["R"])
        elif k == "P":
            w_a += min(v, cnt_b["R"])
            w_b += min(v, cnt_b["S"])
    return w_a, w_a + n - w_b

def main():
    n = int(stdin.readline().strip())
    a = stdin.readline().strip().split(" ")
    b = stdin.readline().strip().split(" ")
    print(" ".join(map(str, min_max_wins(n, a, b))))

if __name__ == "__main__":
    main()
