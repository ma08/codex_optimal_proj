
import sys

def main():
    for line in sys.stdin:
        distance, time, speed = line.split()
        distance = int(distance)
        time = int(time)
        speed = int(speed)
        if (distance / speed) <= time:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()
