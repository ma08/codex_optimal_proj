

import sys

def main():
    n,k = map(int,sys.stdin.readline().split())
    ans = sum(n - i + 1 for i in range(1,k+1) if i <= n)
    print(ans**3)

if __name__ == '__main__':
    main()
