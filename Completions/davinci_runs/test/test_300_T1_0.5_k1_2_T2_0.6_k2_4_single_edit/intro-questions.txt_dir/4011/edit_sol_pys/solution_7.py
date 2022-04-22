import sys

def main():
    n = int(sys.stdin.readline())
    num = list(map(int, sys.stdin.readline().strip().split()))
    f = list(map(int, sys.stdin.readline().strip().split()))
    for i in range(len(num)):
        num[i] = f[num[i]-1] * (10 ** (len(num)-1-i))
    print(sum(num))


if __name__ == '__main__':
    main()
