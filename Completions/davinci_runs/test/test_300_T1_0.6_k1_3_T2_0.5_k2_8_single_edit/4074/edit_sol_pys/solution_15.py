
import sys


def get_min_packages(n, k, l):
    if n <= k and n <= l:
        return min(k, l)
    min_packages = min(k, l)
    for i in range(1, min_packages):
        if n % i == 0 and n // i <= min_packages:
            min_packages = n // i
    return min(k, l, min_packages)

if __name__ == '__main__':
    n_tests = int(sys.stdin.readline())
    for i in range(n_tests):
        n, k, l = [int(x) for x in sys.stdin.readline().split()]
        min_packages = get_min_packages(n, k, l)
        print(min_packages)
