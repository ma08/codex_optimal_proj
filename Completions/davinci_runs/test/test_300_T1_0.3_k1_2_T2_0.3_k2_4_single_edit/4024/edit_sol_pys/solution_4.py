
import sys

def main():
    n, k = map(int, sys.stdin.readline().split())  # n: number of words, k: number of words per line
    s = sys.stdin.readline().strip()
    if k > n:  # if k is greater than n, we can't make any lines
        print(-1)
        return
    elif k == n:
        print(0)
        return
    else:
        print(n*(k-1))

if __name__ == "__main__":
    main()
