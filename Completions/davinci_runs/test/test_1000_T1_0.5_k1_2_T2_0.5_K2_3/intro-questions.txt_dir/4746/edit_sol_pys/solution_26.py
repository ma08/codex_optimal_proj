

import sys

def main():
    input = sys.stdin.readline
    C, n = map(int, input().split()) # capacity and number of stops
    passengers = [0]
    for _ in range(n):
        left, entered, waited = map(int, input().split()) # people who left, entered, and waited at the stop
        passengers.append(passengers[-1] + entered - left + waited) # calculate the number of people on the bus at each stop
    print("possible" if all([0 <= x <= C for x in passengers]) else "impossible") 

if __name__ == '__main__':
    main()
