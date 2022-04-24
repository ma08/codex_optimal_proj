
import sys

def main():
    n, r = map(int, sys.stdin.readline().split())
    r = [r, r]
    for line in sys.stdin:
        a, b = map(int, line.split())
        if a > r[-2]:
            r.append(r[-2])
        else:
            r.append(max(r[-2] - b, 0))
    print(len(r) - 1)

if __name__ == "__main__":
    main()
