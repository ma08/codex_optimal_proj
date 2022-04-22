
import sys


def main():
    n, m = [int(x) for x in sys.stdin.readline().split()]
    lst = [int(x) for x in sys.stdin.readline().split()]
    pairs = 0
    for i in range(n):
        for j in range(i, n):
            if sum(lst[i:j+1]) == m:
                pairs += 1
    print(pairs)

if __name__ == '__main__':
    main()
