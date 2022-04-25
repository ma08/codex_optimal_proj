

from sys import stdin
from collections import Counter
from itertools import combinations

def min_max_wins(n, a, b):
    cnt_a = Counter(a)
    cnt_b = Counter(b)
    w_a = 0
    w_b = 0
    for c_a, c_b in combinations("RSP", 2):
        w_a += min(cnt_a[c_a], cnt_b[c_b])  # cnt_a[c_a]>=cnt_b[c_b]
        w_b += min(cnt_a[c_b], cnt_b[c_a])  # cnt_a[c_b]>=cnt_b[c_a]
    return w_a, w_a + n - w_b

def main():
    n = int(stdin.readline().strip())
    a = stdin.readline().strip()
    b = stdin.readline().strip()
    print(" ".join(map(str, min_max_wins(n, a, b))))

if __name__ == "__main__":
    main()
