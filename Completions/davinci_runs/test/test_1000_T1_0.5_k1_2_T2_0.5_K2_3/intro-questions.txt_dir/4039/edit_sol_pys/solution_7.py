import sys

def main():
    n, m = map(int, input().split())
    a = [0] * m
    b = [0] * m
    for i in range(m):
        a1, b1 = map(int, input().split())
        a[i] = a1
        b[i] = b1

    print(a)
    print(b)

if __name__ == '__main__':
    main()
