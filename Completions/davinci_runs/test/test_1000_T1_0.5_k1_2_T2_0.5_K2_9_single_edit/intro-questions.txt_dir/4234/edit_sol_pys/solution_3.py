

import sys

def main():
    n = int(sys.stdin.readline())
    a = [int(x) for x in sys.stdin.readline().split()]
    b = [int(x) for x in sys.stdin.readline().split()]
    c = [int(x) for x in sys.stdin.readline().split()]
    ans = 0
    for i in range(n):
        ans += b[a[i]-1]
        if i > 0 and a[i-1]+1 == a[i]:
            ans += c[a[i-1]-1]
    print(ans)

if __name__ == '__main__':
    main()
