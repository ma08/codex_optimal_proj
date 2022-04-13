
#
import sys

def main():
    capacity, num_stations = map(int, sys.stdin.readline().split())
    for i in range(num_stations):
        left, entered, waiting = map(int, sys.stdin.readline().split())  # read data from file
        if i == 0:
            people = left  # the first station
        else:
            people += entered - left  # the other station
            if people < 0 or people > capacity or (waiting > 0 and people == capacity):  # check the condition
                print("impossible")
                return
    if people > 0:
        print("impossible")
    else:
        print("possible")

if __name__ == '__main__':
    main()
