
import math

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    print(find(n, a))

def find(n, a):
    res = 0
    for i in range(n):
        res = max(res, a[i])
    return res

if __name__ == '__main__':
    main()
