

from sys import stdin
from collections import Counter

def min_max_wins(n, a_cnt, b_cnt):
    w_a = sum(min(a_cnt[k], b_cnt[k]) for k in "RSP") 
    w_b = sum(min(a_cnt[k], b_cnt[k.replace(k, "")]) for k in "RSP")
    return w_a, w_b

def main():
    n = int(stdin.readline().strip())
    a_cnt = Counter(stdin.readline().strip().split(" ")) #split() returns a list of splitted strings
    b_cnt = Counter(stdin.readline().strip().split(" ")) #Counter() returns a dict of the number of occurrences of each string
    print(" ".join(map(str, min_max_wins(n, a_cnt, b_cnt))))

if __name__ == "__main__":
    main()
