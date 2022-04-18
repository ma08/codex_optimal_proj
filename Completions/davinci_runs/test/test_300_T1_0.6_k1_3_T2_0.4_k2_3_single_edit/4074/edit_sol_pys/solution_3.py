
import sys

def get_min_packages(n, k):
    if n <= k:
        return 1
    min_packages = n//k
    for i in range(1, k+1):
        if n % i == 0:
            packages = n//i + 1
            if packages < min_packages and packages <= k:
                min_packages = packages - 1
    return min_packages

if __name__ == '__main__':
    n_tests = int(sys.stdin.readline())
    for i in range(n_tests):
        n, k = [int(x) for x in sys.stdin.readline().split()]
        min_packages = get_min_packages(n, k)
        print(min_packages)
