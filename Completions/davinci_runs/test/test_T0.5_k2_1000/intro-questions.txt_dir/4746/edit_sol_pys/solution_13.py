#!/usr/bin/env python3

import sys

def main():
    capacity, num_stations = map(int, input().split())
    people = 0
    for i in range(num_stations - 1):
        left, entered, waiting = map(int, input().split())
        people = left + entered
        if people < 0 or people > capacity or (waiting > 0 and people == capacity):
            print("impossible")
            return
    if people > 0:
        print("impossible")
    else:
        print("possible")

if __name__ == '__main__':
    main()
