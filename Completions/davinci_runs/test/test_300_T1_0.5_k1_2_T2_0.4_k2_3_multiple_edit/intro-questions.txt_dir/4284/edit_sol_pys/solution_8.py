
import sys

def main():
    q = int(sys.stdin.readline())
    for _ in range(q):
        k, n, x, y = map(int, sys.stdin.readline().split())
        print(k, n, x, y)

if __name__ == "__main__":
    main()
