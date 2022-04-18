

import sys

def main():
    input = sys.stdin.readline
    C, n = map(int, input().split())
    passengers = [0]
    for _ in range(n):
        left, entered, waited = map(int, input().split())
        passengers.append(passengers[-1] + entered - left + waited)
    print("possible" if all([0 <= x <= C for x in passengers]) else "impossible")

if __name__ == '__main__':
    main()