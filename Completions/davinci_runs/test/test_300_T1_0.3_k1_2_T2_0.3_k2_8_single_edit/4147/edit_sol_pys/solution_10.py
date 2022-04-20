import sys

def main():
    N, A, B, C = map(int, sys.stdin.readline().split())
    l = [int(sys.stdin.readline()) for _ in range(N)]
    l.sort(reverse=True)
    print(solve(l, A, B, C))

def solve(l, A, B, C):
    pass

if __name__ == '__main__':
    main()
