
import sys

def main():
    h, n = map(int, input().split())
    d = list(map(int, input().split()))

    if h <= 0:
        print(1, end="")
        return

    for i in range(n):
        h += d[i]
        if h <= 0:
            print(i + 1, end="")
            return
    print(-1, end="")

if __name__ == '__main__':
    main()
