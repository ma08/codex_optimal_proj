

import sys

def main():
    N = int(input())
    L = [int(i) for i in input().split()]

    if N < 3 or N > 10:
        sys.exit()
    for i in range(N):
        if L[i] < 1 or L[i] > 100:
            sys.exit()

    if max(L) < sum(L) - max(L):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()