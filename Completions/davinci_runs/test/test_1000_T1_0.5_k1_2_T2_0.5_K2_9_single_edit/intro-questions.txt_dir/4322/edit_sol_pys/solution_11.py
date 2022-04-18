
import sys
import math

def main():
    n = int(sys.stdin.readline().strip())
    heights = [int(x) for x in sys.stdin.readline().strip().split()]
    heights.sort()
    balanced = []
    last = None
    for h in heights:
        if last is None or abs(h - last) <= 1:
            balanced.append(h)
            last = h
    print(len(balanced))
    print(' '.join(map(str, balanced)))

if __name__ == "__main__":
    main()
