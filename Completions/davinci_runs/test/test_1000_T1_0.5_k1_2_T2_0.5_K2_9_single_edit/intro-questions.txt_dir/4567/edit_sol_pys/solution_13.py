import sys

def main():
    N = int(sys.stdin.readline().rstrip())
    s = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
    s.sort(reverse=True)
    print(s)

if __name__ == '__main__':
    main()
