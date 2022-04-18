
import sys

def main():
    a, b = [int(x) for x in sys.stdin.readline().split()]
    c = int(sys.stdin.readline())
    d = int(sys.stdin.readline())
    print(max(0, min(a, c) - max(b, d)))

if __name__ == '__main__':
    main()
