import sys

def main():
    sheep = int(sys.stdin.readline())
    wolves = int(sys.stdin.readline())

    if sheep < wolves:
        print("unsafe")
    else:
        print("safe")

if __name__ == '__main__':
    main()
