
import sys
import math

def main():
    n, m = map(int, sys.stdin.readline().strip().split())
    for i in range(n):
        for j in range(m):
            print("*", end="")
        print()



if __name__ == "__main__":
    main()
