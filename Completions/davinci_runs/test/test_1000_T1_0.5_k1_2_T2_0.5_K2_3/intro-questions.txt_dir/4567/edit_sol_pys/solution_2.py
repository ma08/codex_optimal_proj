import sys

def main():
    N = int(sys.stdin.readline().rstrip())
    s = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
    s.sort(reverse=True)
    print(s[0] + s[1] + s[2] if s[0] + s[1] + s[2] < 10 else s[0] + s[1] if s[0] + s[1] < 10 else s[0])

if __name__ == '__main__':
    main()
