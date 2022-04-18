
import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    trees = [int(x) for x in sys.stdin.readline().strip().split()]
    print(sum(trees))
