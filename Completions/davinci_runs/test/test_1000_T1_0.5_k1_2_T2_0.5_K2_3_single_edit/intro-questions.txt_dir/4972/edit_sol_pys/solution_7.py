import sys


def main():
    N = int(sys.stdin.readline())
    if N % 2 == 1:
        print("Weird")
    else:
        if 2 <= N <= 5:
            print("Not Weird")
        elif 6 <= N <= 20:
            print("Weird")
        else:
            print("Not Weird")


if __name__ == "__main__":
    main()
