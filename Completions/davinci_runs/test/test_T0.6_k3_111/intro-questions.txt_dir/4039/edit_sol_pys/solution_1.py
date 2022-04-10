
# https://codeforces.com/problemset/problem/1030/A
import sys

def main():
    n, r = map(int, sys.stdin.readline().split())
    a = []
    b = []
    for i in range(n):
        temp = map(int, sys.stdin.readline().split())
        a.append(temp[0])
        b.append(temp[1])
    for i in range(n):
        if r >= a[i]:
            r += b[i]
            if r < 0:
                print("NO")
                return
    print("YES")


if __name__ == '__main__':
    main()
