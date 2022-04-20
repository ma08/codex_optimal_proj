
import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))
    a = sorted(a)
    b = sorted(b)
    a_i, b_i = 0, 0
    while a_i < n and b_i < m:
        if a[a_i] < b[b_i]:
            a_i += 1
        elif a[a_i] > b[b_i]:
            b_i += 1
        else:
            print(a[a_i])
            a_i += 1
            b_i += 1
    print(-1)

if __name__ == '__main__':
    main()
