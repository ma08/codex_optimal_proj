

import sys

def main():
    t = int(sys.stdin.readline().strip())
    for i in range(t):
        n,k = [int(x) for x in sys.stdin.readline().strip().split()]
        if n%k == 0:
            print(n//k)
        else:
            print(n//k + 1)

if __name__ == "__main__":
    main()