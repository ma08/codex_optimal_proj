
from math import ceil

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))[:n]
    a = sorted(a)
    print(ceil(sum(a[n-k:])/k))


if __name__ == '__main__':
    main()
