
import sys

def main():
    N = int(sys.stdin.readline())
    d = list(map(int, sys.stdin.readline().split()))
    d.sort()
    if N % 2 == 1:
        print(0)
        return
    else:
        count = 0
        for i in range(1, N // 2 + 1):
            if d[i - 1] == d[N // 2 - 1 + i]:
                count += 1
            else:
                break
        print(count)


if __name__ == '__main__':
    main()
