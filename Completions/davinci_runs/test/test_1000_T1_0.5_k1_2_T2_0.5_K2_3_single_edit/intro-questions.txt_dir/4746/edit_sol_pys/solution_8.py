

import sys

def main():
    # capacity, num_stations = map(int, sys.stdin.readline().split())
    capacity = int(input())
    num_stations = int(input())
    for i in range(num_stations):
        # left, entered, waiting = map(int, sys.stdin.readline().split())
        left, entered, waiting = map(int, input().split())
        if i == 0:
            people = left
        else:
            people += entered - left
            if people < 0 or people > capacity or (waiting > 0 and people == capacity):
                print("impossible")
                return
    if people > 0:
        print("impossible")
    else:
        print("possible")

if __name__ == '__main__':
    main()
