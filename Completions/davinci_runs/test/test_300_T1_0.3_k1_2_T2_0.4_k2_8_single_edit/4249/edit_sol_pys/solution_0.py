
import sys

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        ans += b[a[i] - 1]
        if i > 0 and a[i] - a[i - 1] == 1:
            ans += c[a[i - 1] - 1]
    print(ans)

if __name__ == '__main__':
    main()
