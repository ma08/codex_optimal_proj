
import sys

def main():
    n = int(sys.stdin.readline().rstrip())
    a = list(map(int, sys.stdin.readline().rstrip().split()))
    print(min(n, a) + 5)

if __name__ == "__main__":
    main()
