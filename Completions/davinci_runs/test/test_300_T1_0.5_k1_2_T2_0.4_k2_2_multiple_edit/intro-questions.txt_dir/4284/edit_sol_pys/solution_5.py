import sys

def main():
    q = int(sys.stdin.readline())
    for _ in range(q):
        k, n, a, b = map(int, sys.stdin.readline().split())
        print(k, n, a, b)

if __name__ == "__main__":
    main()
