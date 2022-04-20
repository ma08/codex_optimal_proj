
import sys

def main():
    n = int(sys.stdin.readline().strip())
    a = list(map(int, sys.stdin.readline().strip().split()))
    if n == 1:
        print(1)
        return
    if n == 2:
        if a[0] == a[1]:
            print(1)
        else:
            print(2)
        return
    a.sort()
    if a[-1] == a[-2]:
        print(1)
        return
    if a[0] == a[1]:
        print(1)
        return
    if a[1] - a[0] == a[-1] - a[-2]:
        print(2)
        return
    print(3)


if __name__ == '__main__':
    main()
