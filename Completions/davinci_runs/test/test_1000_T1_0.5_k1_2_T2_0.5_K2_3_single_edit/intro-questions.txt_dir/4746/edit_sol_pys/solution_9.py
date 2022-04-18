

import sys

def main():
    input = sys.stdin.readline
    C, n = map(int, input().split()) # C = capacity, n = number of stops
    passengers = [0]
    for _ in range(n):
        left, entered, waited = map(int, input().split()) # left = people who left, entered = people who entered, waited = people who waited
        passengers.append(passengers[-1] + entered - left + waited)
    print("possible" if all([0 <= x <= C for x in passengers]) else "impossible")

if __name__ == '__main__':
    main()
