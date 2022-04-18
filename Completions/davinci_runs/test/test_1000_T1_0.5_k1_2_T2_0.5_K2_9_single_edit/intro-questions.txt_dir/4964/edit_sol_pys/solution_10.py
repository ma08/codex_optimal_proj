# https://open.kattis.com/problems/horror

import sys

def main():
    N, H, L = map(int, sys.stdin.readline().split())
    horror = set(map(int, sys.stdin.readline().split()))
    sim = {}
    for i in range(L):
        a, b = map(int, sys.stdin.readline().split())
        sim.setdefault(a, set()).add(b)
        sim.setdefault(b, set()).add(a)
    HI = [float('inf')] * N
    for i in range(N):
        if i in horror:
            HI[i] = float('inf')
        else:
            HI[i] = min([HI[j] for j in sim[i]] + [0]) + 1
    print(HI.index(max(HI)))

if __name__ == '__main__':
    main()
