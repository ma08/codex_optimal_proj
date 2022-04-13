
import sys

def main():
    n = int(sys.stdin.readline().strip())
    heights = [int(x) for x in sys.stdin.readline().strip().split()][:n]
    heights.sort()
    balanced_heights = []
    last = None
    for h in heights:
        if last is None or abs(h - last) <= 1:
            balanced_heights.append(h)
            last = h
    print(len(balanced_heights))
    print(' '.join(map(str, balanced_heights)))

if __name__ == "__main__":
    main()
