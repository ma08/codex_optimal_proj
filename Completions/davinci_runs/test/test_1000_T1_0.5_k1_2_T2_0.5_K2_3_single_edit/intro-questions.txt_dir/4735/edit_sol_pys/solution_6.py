
import sys

def is_launch_window(year):
    if year % 26 == 0:
        print("yes", end='')
    elif year % 26 == 2:
        print("yes", end='')
    elif year % 26 == 4:
        print("yes", end='')
    elif year % 26 == 6:
        print("yes", end='')
    elif year % 26 == 8:
        print("yes", end='')
    elif year % 26 == 10:
        print("yes", end='')
    elif year % 26 == 12:
        print("yes", end='')
    elif year % 26 == 14:
        print("yes", end='')
    elif year % 26 == 16:
        print("yes", end='')
    elif year % 26 == 18:
        print("yes", end='')
    elif year % 26 == 20:
        print("yes", end='')
    elif year % 26 == 22:
        print("yes", end='')
    elif year % 26 == 24:
        print("yes", end='')
    elif year % 26 == 26:
        print("yes", end='')
    else:
        print("no", end='')

def main():
    year = int(sys.stdin.readline())
    is_launch_window(year)

if __name__ == "__main__":
    main()
