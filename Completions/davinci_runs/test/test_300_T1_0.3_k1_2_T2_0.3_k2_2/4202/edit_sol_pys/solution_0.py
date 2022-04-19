
import sys

def main():
    l, r = map(int, sys.stdin.readline().split()) # read line and split by space
    mod = 2019
    min_mod = mod
    for i in range(l, r): # loop from l to r
        for j in range(i+1, r+1): # loop from i+1 to r+1
            min_mod = min(min_mod, (i*j)%mod) # update min_mod
    print(min_mod)

if __name__ == '__main__':
    main()
