import sys

def main():
    q = int(sys.stdin.readline().strip())
    for _ in range(q):
        a, b, c = map(int, sys.stdin.readline().split())
        print(max(a, b, c) - min(a, b, c))

if __name__ == '__main__':
    main()
