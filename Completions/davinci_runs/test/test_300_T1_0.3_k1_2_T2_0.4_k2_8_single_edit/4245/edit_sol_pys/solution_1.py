import sys

def main():
    line = sys.stdin.readline().rstrip()
    A, B = map(int, line.split())
    print(A * B)

if __name__ == '__main__':
    main()
