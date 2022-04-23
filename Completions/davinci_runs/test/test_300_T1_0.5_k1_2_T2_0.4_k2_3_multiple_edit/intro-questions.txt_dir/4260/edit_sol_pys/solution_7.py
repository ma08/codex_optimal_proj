import sys

def main():
    input = sys.stdin.readline
    T, X = map(int, input().split())
    print(T / X)

if __name__ == '__main__':
    main()
