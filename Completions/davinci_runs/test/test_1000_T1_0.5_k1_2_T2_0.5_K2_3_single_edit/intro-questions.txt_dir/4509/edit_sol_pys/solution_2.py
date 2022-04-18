import sys

def main():
    n = int(sys.stdin.readline())
    for _ in range(n):
        n, k = map(int, sys.stdin.readline().split(" "))
        print(n * k + 1)

if __name__ == '__main__':
    main()
