
import sys

def main():
    N = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    a.sort()
    if N % 2 == 1:
        print(0)
        return
    else:
        count = 0
        for i in range(1, N // 2 + 1):
            if a[i - 1] == a[N // 2 - 1 + i]:
                count += 1
            else:
                break
        print(count)


if __name__ == '__main__':
    main()
