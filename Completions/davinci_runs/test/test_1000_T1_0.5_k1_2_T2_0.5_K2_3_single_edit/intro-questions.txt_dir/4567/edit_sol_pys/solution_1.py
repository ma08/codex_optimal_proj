
import sys

def main():
    N = int(sys.stdin.readline().rstrip())
    s = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
    s.sort(reverse=True)
    if s[0] >= 10:
        print(s[0])
    elif s[0] + s[1] >= 10:
        print(s[0] + s[1])
    else:
        print(sum(s[:3]))

if __name__ == '__main__':
    main()
