# -*- coding: utf-8 -*-



def main():
    n, m = map(int, input().split())

    a = [0] * (m+1)
    for i in range(n):
        a[i] = int(input())

    print(a)

if __name__ == "__main__":
    main()
