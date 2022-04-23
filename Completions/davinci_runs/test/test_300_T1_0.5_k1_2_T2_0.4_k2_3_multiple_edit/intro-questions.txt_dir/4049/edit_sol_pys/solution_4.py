
from sys import stdin
from collections import Counter
from itertools import combinations

def min_max_wins(n, a, b):
    cnt_a = Counter(a)
    cnt_b = Counter(b)
    w_a = 0
    w_b = 0
    for k in cnt_a.keys():
        w_a += min(cnt_a[k], cnt_b[k])
        w_b += min(cnt_a[k], cnt_b[k])
    return w_a, w_a + n - w_b

def main():
    n = int(stdin.readline().strip())
    a = stdin.readline().strip().split(" ")
    b = stdin.readline().strip().split(" ")
    print(" ".join(map(str, min_max_wins(n, a, b))))

if __name__ == "__main__":
    main()
