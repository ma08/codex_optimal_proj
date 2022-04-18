
import sys

def main():
    q = int(sys.stdin.readline().strip())
    for _ in range(q):
        a, b, c = map(int, sys.stdin.readline().strip().split())
        print(max(max(a, b), c) + min(min(a, b), c))

if __name__ == '__main__':
    main()
