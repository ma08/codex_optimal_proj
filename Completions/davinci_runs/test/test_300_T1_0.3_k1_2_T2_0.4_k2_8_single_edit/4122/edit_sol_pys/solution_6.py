import sys

def main():
    h, n = map(int, input().split())
    d = list(map(int, input().split()))

    if h <= 0:
        print(1)
        return

    for i in range(n):
        h += d[i]
        if h <= 0:
            print(i + 1)
            return
    print(-1)

if __name__ == '__main__':
    main()
