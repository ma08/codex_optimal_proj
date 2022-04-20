
import sys

def main():
    N, A, B = map(int, sys.stdin.readline().rstrip().split())
    print(min(N * A, B))

if __name__ == '__main__':
    main()
