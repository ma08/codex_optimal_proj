
import sys

def is_launch_win(y):
    return y % 26 == 2

def main():
    year = int(sys.stdin.readline())
    print("yes" if is_launch_win(year) else "no")

if __name__ == "__main__":
    main()
