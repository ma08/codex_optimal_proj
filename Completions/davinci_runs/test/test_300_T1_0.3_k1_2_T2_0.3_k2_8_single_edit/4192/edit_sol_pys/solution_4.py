import sys

def main():
    d, t, s = map(int, sys.stdin.readline().split())
    if d / s <= t:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
