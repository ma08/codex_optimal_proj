
import sys

def main():
    n = int(input())
    a = list(map(int, input().split()))

    a.sort(reverse=True)

    for i in range(1, n):
        a[i] += a[i - 1]

    for i in range(n):
        if a[i] * 2 >= a[0]:
            print(i + 1)
            break

if __name__ == '__main__':
    main()
