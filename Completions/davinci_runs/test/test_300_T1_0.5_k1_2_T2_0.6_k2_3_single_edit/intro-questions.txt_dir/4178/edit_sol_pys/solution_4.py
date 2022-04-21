import sys

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    if n == 1 and a[0] == k:
        print('Yes')
        return
    for i in range(n):
        if a[i] < k:
            a[i] = 0
        else:
            a[i] -= k
    if a == [0] * n:
        print('Yes')
        sys.exit(0)
    for i in range(n-1):
        if a[i] != a[i+1]:
            print('No')
            sys.exit(0)
    print('Yes') 


if __name__ == '__main__':
    main()
