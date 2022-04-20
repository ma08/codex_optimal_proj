
import sys
import math

def main():
    N = int(sys.stdin.readline().rstrip())
    A = int(sys.stdin.readline().rstrip())
    B = int(sys.stdin.readline().rstrip())
    print(min(N*A, B), end="")

if __name__ == '__main__':
    main()
