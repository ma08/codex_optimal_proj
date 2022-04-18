
import sys

def main():
    sheep_count, wolves_count = map(int, sys.stdin.readline().split())
    if sheep_count < wolves_count:
        print("unsafe")
    else:
        print("safe")

if __name__ == '__main__':
    main()
