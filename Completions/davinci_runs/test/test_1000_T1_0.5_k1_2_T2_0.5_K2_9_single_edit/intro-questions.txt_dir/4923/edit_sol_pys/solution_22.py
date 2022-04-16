
import sys
from collections import Counter

def main():
    n = int(sys.stdin.readline())
    rolls = list(map(int, sys.stdin.readline().split()))
    for i in rolls:
        print(i)

if __name__ == "__main__":
    main()
