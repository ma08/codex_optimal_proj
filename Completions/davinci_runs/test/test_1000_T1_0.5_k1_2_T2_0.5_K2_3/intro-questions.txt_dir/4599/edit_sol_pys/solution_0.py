# -*- coding: utf-8 -*-



def main():
    n, m = map(int, input().split())

    a = [0] * (n+1)
    for i in range(n):
        a[i] = int(input())

    print(sum(a))

if __name__ == "__main__":
    main()
