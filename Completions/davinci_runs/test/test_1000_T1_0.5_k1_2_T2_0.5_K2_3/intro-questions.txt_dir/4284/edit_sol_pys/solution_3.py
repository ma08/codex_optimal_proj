
import sys

def main():
    n = int(sys.stdin.readline())
    for _ in range(n):
        a = list(map(int, sys.stdin.readline().split()))
        print(a)

if __name__ == "__main__":
    main()
