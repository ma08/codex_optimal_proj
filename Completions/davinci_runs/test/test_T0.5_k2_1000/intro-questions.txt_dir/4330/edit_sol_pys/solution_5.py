import sys

def main():
    a, b = map(int, sys.stdin.readline().rstrip().split())
    if a < b:
        a, b = b, a
    if a - b == 0:
        print(0)
    elif a - b < b:
        print(a - b)
    else:
        print("IMPOSSIBLE")

if __name__ == '__main__':
    main()
