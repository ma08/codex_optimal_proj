
import sys

def main():
    n = int(sys.stdin.readline())
    trees = [int(x) for x in sys.stdin.readline().split()]
    trees.sort()
    if n == 1:
        print(trees[0])
    else:
        max_days = 0
        for i in range(n):
            max_days = max(max_days, trees[i] + n - i - 1)
        print(max_days)

if __name__ == '__main__':
    main()
