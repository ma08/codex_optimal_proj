
import sys

def is_launch_window(year):
    return "yes" if year % 26 == 2 else "no"


if __name__ == '__main__':
    print(is_launch_window(int(sys.stdin.readline().strip())))
