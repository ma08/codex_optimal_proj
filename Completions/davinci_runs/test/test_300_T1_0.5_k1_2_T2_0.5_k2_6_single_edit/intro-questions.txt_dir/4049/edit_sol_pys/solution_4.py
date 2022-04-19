

from sys import stdin
from collections import Counter
from itertools import combinations

def main():
    n = int(input())
    a = input().split(" ")
    b = input().split(" ")
    cnt_a = Counter(a)
    cnt_b = Counter(b)
    w_a = w_b = 0
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
    print(w_a, w_a + n - w_b)

if __name__ == '__main__':
    main()
