import sys

def main():
    n, k = map(int, input().split())
    a, b = zip(*(map(int, input().split()) for _ in range(n)))
    c = [0] * (10**5 + 1)
    for i in range(n):
        c[a[i]] += b[i]
    for i in range(1, 10**5 + 1):
        if k <= c[i]:
            print(i)
            break
        k -= c[i]

if __name__ == '__main__':
    main()
