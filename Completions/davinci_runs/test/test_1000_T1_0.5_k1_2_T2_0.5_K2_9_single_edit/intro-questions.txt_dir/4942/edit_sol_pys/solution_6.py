

import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    trees = [int(x) for x in sys.stdin.readline().strip().split()][::-1]
    count = 0
    for i in range(n):
        count += trees[i]
    print(count)
