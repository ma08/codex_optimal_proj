import sys

def main():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))
    c = list(map(int, sys.stdin.readline().split()))
    ans = sum(b)
    for i in range(n - 1):
        if a[i + 1] - a[i] == 1:
            ans += c[a[i] - 1]
    print(ans)

if __name__ == '__main__':
    main()
