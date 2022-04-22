
import sys

def main():
    sheep, wolves = map(int, sys.stdin.readline().split())

    if sheep < wolves:
        print("Unsafe")
    else:
        print("Safe")

if __name__ == '__main__':
    main()
