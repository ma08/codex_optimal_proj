import sys

def main():
    N, T, M = map(int, sys.stdin.readline().split())
    print(N * T * M // 60)

if __name__ == "__main__":
    main()
