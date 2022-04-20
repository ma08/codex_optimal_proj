
import sys

def main():
    n = int(input())
    if n == 1:
        print(0)
        exit()
    a = [0] * n
    a[1] = 0
    for i in range(2, n):
        a[i] = a[i - 1] + 1
        if i % 2 == 0:
            a[i] = min(a[i], a[i // 2] + 1)
        if i % 3 == 0:
            a[i] = min(a[i], a[i // 3] + 1)
    print(a[n - 1])

if __name__ == '__main__':
    main()
