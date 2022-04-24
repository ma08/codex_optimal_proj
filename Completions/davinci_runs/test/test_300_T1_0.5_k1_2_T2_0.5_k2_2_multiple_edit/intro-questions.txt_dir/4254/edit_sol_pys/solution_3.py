
import sys

def main():
    sheep, wolves, sheep_per_wolf = map(int, sys.stdin.readline().split())

    if sheep < wolves * sheep_per_wolf:
        print("unsafe")
    else:
        print("safe")

if __name__ == '__main__':
    main()
