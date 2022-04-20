import sys

def main():
    n = int(sys.stdin.readline())
    num = list(map(int, sys.stdin.readline().strip()))  # [1, 2, 3, 4, 5]
    f = list(map(int, sys.stdin.readline().strip().split()))  # [1, 2, 3, 4, 5]

    for i in range(len(num)):
        num[i] = f[num[i]-1]  # [1, 2, 3, 4, 5] -> [1, 2, 3, 4, 5]

    print(''.join(map(str, num)))


if __name__ == '__main__':
    main()
