
import sys

def main():
    n = int(sys.stdin.readline())
    a = [int(x) for x in sys.stdin.readline().split()]
    print(n)
    print(*a)

if __name__ == '__main__':
    main()
