import sys

def main():
    sheep, wolves = map(int, input().split())
    if sheep < wolves:
        print("unsafe")
    else:
        print("safe")

if __name__ == '__main__':
    main()
