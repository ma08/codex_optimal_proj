
import sys

def main():
    k, x = list(map(int, sys.stdin.readline().split()))

    for i in range(k):
        print(x - k + 1 + i, end=" ")



if __name__ == "__main__":
    main()
