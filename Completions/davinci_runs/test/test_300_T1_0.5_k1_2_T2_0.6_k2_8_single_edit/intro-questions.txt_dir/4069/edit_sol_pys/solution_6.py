
import sys

def main():
    n = int(sys.stdin.readline().rstrip())
    a = list(map(int, sys.stdin.readline().rstrip().split()))
    b = list(map(int, sys.stdin.readline().rstrip().split()))
    c = list(map(int, sys.stdin.readline().rstrip().split()))
    ans = 0
    for i in range(n):
        ans += b[a[i] - 1]
        if i >= 1 and a[i] - a[i - 1] == 1:
            ans += c[a[i - 1] - 1]
    print(ans)

if __name__ == '__main__':
    main()
