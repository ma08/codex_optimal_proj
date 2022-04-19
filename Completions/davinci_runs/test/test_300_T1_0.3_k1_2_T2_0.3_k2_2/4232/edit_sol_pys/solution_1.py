

import sys

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    print(a[k-1])

if __name__ == '__main__':
    main()
