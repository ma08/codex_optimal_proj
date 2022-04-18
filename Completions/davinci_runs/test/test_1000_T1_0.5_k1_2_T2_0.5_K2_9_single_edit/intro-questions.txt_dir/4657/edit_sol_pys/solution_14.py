
import sys

def main():
    q = int(input())
    for _ in range(q):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        if k > n:
            print('NO')
            continue
        if k == 1:
            if sum(a) % 2 == 0:
                print('NO')
                continue
            print('YES')
            print(n)
            continue
        if k == n:
            if sum(a) % 2 == 0:
                print('NO')
                continue
            print('YES')
            for i in range(1, n):
                print(i, end=' ')
            print(n)
            continue
        print('YES')
        if sum(a) % 2 == 0:
            print(1, end=' ')
            for i in range(2, k):
                print(i, end=' ')
            print(n)
            continue
        for i in range(1, k):
            print(i, end=' ')
        print(n)
            
if __name__ == '__main__':
    main()
