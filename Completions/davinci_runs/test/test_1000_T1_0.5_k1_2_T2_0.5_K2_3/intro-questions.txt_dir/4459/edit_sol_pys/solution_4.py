import sys

def main():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    a.sort()
    ans = 0
    for i in range(n):
        if a[i] < i + 1:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()
