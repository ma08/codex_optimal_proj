
import sys

def main():
    line = sys.stdin.readline()
    distance, time, speed = map(int, line.split())
    if (distance / speed) <= time or distance % speed == 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
