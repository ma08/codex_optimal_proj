import sys

def main():
    n = int(sys.stdin.readline())
    t = list(map(int, sys.stdin.readline().split())

    t.sort(reverse=True)

    print(t)

if __name__ == '__main__':
    main()
