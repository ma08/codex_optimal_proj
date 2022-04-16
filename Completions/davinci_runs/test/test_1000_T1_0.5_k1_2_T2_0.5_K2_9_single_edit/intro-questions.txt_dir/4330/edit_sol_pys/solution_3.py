import sys

def main():
    a, b = map(int, sys.stdin.readline().rstrip().split())
    if a < b:
        a, b = b, a
    if a - b == b:
        print(int(0))
    elif a - b < b:
        print(int(a - b))
    else:
        print("IMPOSSIBLE")

if __name__ == '__main__':
    main()
