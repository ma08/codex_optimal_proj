
import math
import sys

def main():
    N = int(sys.stdin.readline().strip())
    A = [int(x) for x in sys.stdin.readline().strip().split()]
    for i in range(N):
        print(A[i])

if __name__ == "__main__":
    main()
