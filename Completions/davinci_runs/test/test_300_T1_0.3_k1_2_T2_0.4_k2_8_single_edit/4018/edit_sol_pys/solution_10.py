
import sys

def main():
    n, k = map(int, sys.stdin.readline().split())
    s = sys.stdin.readline().strip()
    if n == k:
        print(0)
        return
    if k > n * (n + 1) / 2:
        print(-1)
        return
    # if n > k:
    #     print(n - k)
    #     return
    if k % n == 0:
        print(0)
        return
    print(n - k % n)

if __name__ == '__main__':
    main()
