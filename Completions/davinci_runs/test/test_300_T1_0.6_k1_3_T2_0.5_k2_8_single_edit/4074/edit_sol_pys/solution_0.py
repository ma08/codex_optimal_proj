

import sys

def get_max_packages(n, k):
    count = 0
    while n > 0:
        n -= k
        count += 1
    return count

if __name__ == '__main__':
    n_tests = int(sys.stdin.readline())
    for i in range(n_tests):
        n, k = [int(x) for x in sys.stdin.readline().split()]
        max_packages = get_max_packages(n, k)
        print(max_packages)
