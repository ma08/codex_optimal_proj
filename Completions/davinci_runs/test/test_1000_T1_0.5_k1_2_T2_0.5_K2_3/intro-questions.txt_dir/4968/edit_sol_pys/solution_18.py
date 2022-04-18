

import sys

def main():
    n, s, r = [int(i) for i in sys.stdin.readline().split()]  # number of seats, number of broken seats, number of reserve seats
    broken = [int(i) for i in sys.stdin.readline().split()]
    reserve = [int(i) for i in sys.stdin.readline().split()]
    total = 0  # total number of passengers that can't sit down
    for i in broken:
        if i == 1:  # first seat
            if 2 in reserve:  # if the second seat is reserve
                reserve.remove(2)
            else:
                total += 1
        elif i == n:
            if n-1 in reserve:
                reserve.remove(n-1)
            else:
                total += 1
        else:
            if i-1 in reserve:
                reserve.remove(i-1)
            elif i+1 in reserve:
                reserve.remove(i+1)
            else:
                total += 1
    print(total)

if __name__ == "__main__":
    main()
