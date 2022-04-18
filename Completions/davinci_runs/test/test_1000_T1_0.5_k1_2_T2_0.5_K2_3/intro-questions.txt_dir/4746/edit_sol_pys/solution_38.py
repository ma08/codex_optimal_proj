
import sys

def main():
    read_line = sys.stdin.readline
    C, n = map(int, read_line().split())[0:2]
    passengers = [0]
    for _ in range(n):
        left, entered, waited = map(int, read_line().split())[0:3]
        passengers.append(passengers[-1] + entered - left + waited)
    print("possible" if all([0 <= x <= C for x in passengers]) else "impossible")

if __name__ == '__main__':
    main()
