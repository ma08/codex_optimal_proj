
import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    trees = [int(x) for x in sys.stdin.readline().strip().split()]
    count = 0
    while n > 0:
        n -= 1
        count += trees[n]
    print(count)
