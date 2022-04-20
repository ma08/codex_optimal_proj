import sys

def main():
    n = int(sys.stdin.readline())
    lengths = list(map(int, sys.stdin.readline().split()))
    if max(lengths) < sum(lengths) - max(lengths):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
