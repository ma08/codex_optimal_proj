
#

import sys
sys.setrecursionlimit(10**6)

def main():
    t = int(input().strip())

    for _ in range(t):
        n = int(input().strip())

        ans = (n-1)//2
        print(ans)


if __name__ == '__main__':
    main()
