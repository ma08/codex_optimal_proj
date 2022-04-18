
import sys

def main():
    sheeps, wolves = map(int, sys.stdin.readline().split())

    if sheeps < wolves:
        print("unsafe")
    else:
        print("safe")

if __name__ == '__main__':
    main()
