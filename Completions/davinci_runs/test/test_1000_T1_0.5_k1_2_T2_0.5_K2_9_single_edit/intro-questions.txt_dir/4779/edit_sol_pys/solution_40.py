
import sys

def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
    a.sort()
    ans = 0
    cur = 0
    for i in range(n):
        cur += a[i]
        ans = max(ans, cur * a[i])
    print(ans, end="")

if __name__ == '__main__':
    main()
