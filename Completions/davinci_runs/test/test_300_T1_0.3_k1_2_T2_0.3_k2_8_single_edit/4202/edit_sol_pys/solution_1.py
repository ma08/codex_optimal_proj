

import sys

def main():
    l, r = map(int, sys.stdin.readline().split())
    mod = 2019
    min_mod = mod
    for i in range(l, r+1):
        for j in range(i+1, r+2):
            min_mod = min(min_mod, (i*j)%mod)
    print(min_mod)

if __name__ == '__main__':
    main()
