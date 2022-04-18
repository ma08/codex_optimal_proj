# -*- coding: utf-8 -*-



def main():
    n, m = map(int, input().split())

    a = [0] * m
    for i in range(m):
        a[i] = int(input()) - 1

    print(n - m)

if __name__ == "__main__":
    main()
