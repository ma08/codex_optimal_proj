import sys

def main():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    a.sort()
    for i in range(1, n):
        a[i] += a[i - 1]
    q = int(sys.stdin.readline())
    for _ in range(q):
        m = int(sys.stdin.readline())
        ans = 0
        if m < a[0]:
            ans = -1
        else:
            for i in range(n):
                if m < a[i]:
                    ans = i
                    break
        print(ans)


if __name__ == '__main__':
    main()
