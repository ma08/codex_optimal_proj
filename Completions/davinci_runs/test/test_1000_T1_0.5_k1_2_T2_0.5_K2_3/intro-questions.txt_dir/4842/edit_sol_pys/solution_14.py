import sys


def main():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        for j in range(n):
            if a[i] < a[j]:
                a[i], a[j] = a[j], a[i]
    for i in range(n):
        print(a[i])

main()
