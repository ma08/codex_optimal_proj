
import sys

def main():
    a, b, c, d = map(int, sys.stdin.readline().split())
    cnt = 0

    for i in range(a, b+1):
        if i % c != 0 and i % d != 0:
            cnt += 1

    print(cnt)

if __name__ == '__main__':
    main()
