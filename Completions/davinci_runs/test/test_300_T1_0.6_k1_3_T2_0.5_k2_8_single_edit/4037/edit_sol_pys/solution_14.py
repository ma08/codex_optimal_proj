
import sys

def main():
    n, r = map(int, sys.stdin.readline().split())
    r = [r - 1]
    for line in sys.stdin:
        a, b = map(int, line.split())
        if a > r[-1] + 1:
            r.append(r[-1] + 1)
        else:
            r.append(max(r[-1] - b + 1, 0))
    print(len(r) - 1)

if __name__ == "__main__":
    main()
