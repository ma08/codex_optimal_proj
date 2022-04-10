
# this is a comment
import sys

def main():
    n, r = map(int, sys.stdin.readline().split())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = map(int, sys.stdin.readline().split())
    for i in range(n):
        if r >= a[i]:
            r += b[i]
            if r < 0:
                print("NO")
                return
    print("YES")


if __name__ == '__main__':
    main()
