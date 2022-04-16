
import sys

def is_launch_window(year):
    return year % 26 == 2

def main():
    year = int(sys.stdin.readline())
    print("yes" if is_launch_window(year) else "no")

if __name__ == "__main__":
    main()
