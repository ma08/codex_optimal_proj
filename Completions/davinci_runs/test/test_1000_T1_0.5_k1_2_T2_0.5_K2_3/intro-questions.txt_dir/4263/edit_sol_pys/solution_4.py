import sys

def main():
    N, M = map(int, sys.stdin.readline().rstrip().split())
    A = list(map(int, sys.stdin.readline().rstrip().split()))
    B = list(map(int, sys.stdin.readline().rstrip().split()))

    count = 0
    for b in B:
        if b in A:
            count += 1

    print(count)


if __name__ == '__main__':
    main()
