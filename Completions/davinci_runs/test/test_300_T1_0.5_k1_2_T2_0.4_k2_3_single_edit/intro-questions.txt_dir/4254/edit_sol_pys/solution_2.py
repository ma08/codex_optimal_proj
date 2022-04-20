
import sys

def main():
    sheep, wolves = map(int, sys.stdin.readline().split())  # input

    if sheep < wolves:
        print("unsafe")  # output
    else:
        print("safe")  # output

if __name__ == '__main__':
    main()
