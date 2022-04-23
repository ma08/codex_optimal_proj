import sys

def main():
    sheep, wolves, chickens = map(int, sys.stdin.readline().split())
    if sheep < wolves or chickens < wolves:
        print("unsafe")
    else:
        print("safe")

if __name__ == '__main__':
    main()
