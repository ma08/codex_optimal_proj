import sys

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = [0] * n
    for i in range(n):
        c.append((a[i] + b[i]) % n)
    c.sort()
    for i in range(n):
        print(c[i], end=' ')

if __name__ == '__main__':
    main()
