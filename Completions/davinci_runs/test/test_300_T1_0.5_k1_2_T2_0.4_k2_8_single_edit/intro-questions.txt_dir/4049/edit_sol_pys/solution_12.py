

from sys import stdin
from collections import Counter
from itertools import combinations

def min_max_wins(n, a, b):
    cnt_a = Counter(a)
    cnt_b = Counter(b)
    w_a = 0
    w_b = 0
    for k, v in cnt_a.items():
        if k == "R" and cnt_b["S"] > 0:
            w_a += min(v, cnt_b["S"]) 
            cnt_b["S"] -= min(v, cnt_b["S"])
        elif k == "S" and cnt_b["P"] > 0:
            w_a += min(v, cnt_b["P"])
            cnt_b["P"] -= min(v, cnt_b["P"])
        elif k == "P" and cnt_b["R"] > 0:
            w_a += min(v, cnt_b["R"])
            cnt_b["R"] -= min(v, cnt_b["R"])
    for k, v in cnt_b.items():
        if k == "R" and cnt_a["S"] > 0:
            w_b += min(v, cnt_a["S"]) 
            cnt_a["S"] -= min(v, cnt_a["S"])
        elif k == "S" and cnt_a["P"] > 0:
            w_b += min(v, cnt_a["P"])
            cnt_a["P"] -= min(v, cnt_a["P"])
        elif k == "P" and cnt_a["R"] > 0:
            w_b += min(v, cnt_a["R"])
            cnt_a["R"] -= min(v, cnt_a["R"])
    return w_a, w_a + n - w_b

def main():
    n = int(stdin.readline().strip())
    a = stdin.readline().strip().split(" ")
    b = stdin.readline().strip().split(" ")
    print(" ".join(map(str, min_max_wins(n, a, b))))

if __name__ == "__main__":
    main()
