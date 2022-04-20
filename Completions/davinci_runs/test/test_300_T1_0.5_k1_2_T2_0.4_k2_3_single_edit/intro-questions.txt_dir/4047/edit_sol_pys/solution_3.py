
import sys

def main():
    n = int(input())
    x = list(map(int, input().split()))
    x.sort()
    print(0 if n % 2 == 1 else x[n//2] - x[n//2 - 1])

if __name__ == "__main__":
    main()
