
import sys

def main():
    n, k = map(int, sys.stdin.readline().split())  # read n, k
    t = sys.stdin.readline().strip()  # read t
    print(t * (k // n) + t[:k % n])  # print t * (k // n) + t[:k % n]

if __name__ == "__main__":
    main()
