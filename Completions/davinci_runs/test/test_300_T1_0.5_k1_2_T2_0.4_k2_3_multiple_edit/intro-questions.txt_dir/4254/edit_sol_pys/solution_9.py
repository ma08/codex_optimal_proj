
import sys

def main():
    sheep, wolf = map(int, input().split())

    if sheep < wolf:
        print("unsafe")
    else:
        print("safe")

if __name__ == '__main__':
    main()
