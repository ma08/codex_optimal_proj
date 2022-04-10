

import sys

def main():
    N = int(sys.stdin.readline())
    d = [int(x) for x in sys.stdin.readline().rstrip().split()]
    d.sort()

    l = 0
    r = N//2
    ans = 0
    while l <= r:
        m = (l+r)//2
        if d[m] == d[N//2]:
            ans += 1
            l += 1
        elif d[m] < d[N//2]:
            l += 1
        else:
            r -= 1
    print(ans)

if __name__ == '__main__':
    main()