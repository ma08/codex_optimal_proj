

#import sys
#sys.setrecursionlimit(10**6)

def main():
    n, k, q = map(int, input().split())
    a = [int(input()) for i in range(q)]
    p = [k] * n
    for i in range(q):
        for j in range(n):
            if j + 1 != a[i]:
                p[j] -= 1
    for i in range(n):
        if p[i] > 0:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()