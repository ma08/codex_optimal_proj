
import sys

def main():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))

    ans = 0
    for i in range(1, n):
        if a[i-1] > a[i]:
            ans += a[i-1] - a[i]
            a[i] = a[i-1]

    print(ans)

if __name__ == "__main__":
    main()
