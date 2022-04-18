import sys

def main():
    A, B = map(int, sys.stdin.readline().split())
    print(int(A * B * 0.5))

if __name__ == '__main__':
    main()
