

import sys

def main():
    N, H, L = map(int, input().split())
    horror = set(map(int, input().split()))
    sim = {}
    for i in range(L):
        a, b = map(int, input().split())
        sim.setdefault(a, set()).add(b)
        sim.setdefault(b, set()).add(a)
    HI = [0] * N
    for i in range(N):
        if i in horror:
            HI[i] = 0
        else:
            HI[i] = max([HI[j] for j in sim[i]] + [float('inf')]) + 1
    print(HI.index(max(HI)))

if __name__ == '__main__':
    main()
