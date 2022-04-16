import sys

def main():
    n = int(sys.stdin.readline())
    bricks = [int(x) for x in sys.stdin.readline().split()]
    print(len(set(bricks)))

if __name__ == "__main__":
    main()
