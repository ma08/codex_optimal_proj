
import sys

def main():
    n, r = map(int, sys.stdin.readline().split())
    r = [0]
    for line in sys.stdin:
        a, b = map(int, line.split())
        r.append(max(r[-1] - b, 0))
        if a > r[-1]: r[-1] = r[-2]
    print(len(r))

if __name__ == "__main__":
    main()
