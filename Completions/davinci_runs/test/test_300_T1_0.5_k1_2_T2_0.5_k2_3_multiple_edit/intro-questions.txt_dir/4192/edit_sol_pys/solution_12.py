

import sys

def main():
    line = sys.stdin.readline()
    distance, time, speed = line.split(" ")
    distance = int(distance)
    time = int(time)

    speed = int(speed)
    if (distance / speed) <= time:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
