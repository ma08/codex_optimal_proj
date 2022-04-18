

import sys

def main():
    input = sys.stdin.readline
    C, n = map(int, input().split())
    passengers = [0] * (n + 1)
    for _ in range(n):
        left, entered, waited = map(int, input().split())
        passengers[i+1] = passengers[i] + entered - left + waited
    print("possible" if all([0 <= x <= C for x in passengers]) else "impossible")

if __name__ == '__main__':
    main()
