import sys

def main():
    q = int(sys.stdin.readline())
    for _ in range(q):
        k, n, a, b = map(int, sys.stdin.readline().split())
        if a <= b:
            print(-1)
            continue
        if k < a:
            print(0)
            continue
        if k >= a + b:
            print(n)
            continue
        print(min(n, (k - a) // (a - b) + 1))

if __name__ == "__main__":
    main()
