
import sys

def main():
    N = int(sys.stdin.readline().rstrip())
    s = [int(input()) for _ in range(N)]
    s.sort(reverse=True)
    if s[0] >= 10:
        print(s[0])
    elif s[0] + s[1] >= 10:
        print(s[0] + s[1])
    else:
        print(s[0] + s[1] + s[2]) 

if __name__ == '__main__':
    main()
