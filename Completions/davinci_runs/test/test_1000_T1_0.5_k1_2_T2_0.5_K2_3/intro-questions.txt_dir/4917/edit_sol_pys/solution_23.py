

import sys

def solve(times):
    pass

def main():
    n = int(sys.stdin.readline().strip())
    times = []
    for _ in range(n):
        times.append(tuple(map(int, sys.stdin.readline().strip().split())))
    print(solve(times))

if __name__ == "__main__":
    main()
