
# SOLUTION

#!/usr/bin/python3

from sys import stdin

def main():
    t = int(stdin.readline())
    for i in range(t):
        n, k = map(int, stdin.readline().split())
        a = list(map(int, stdin.readline().split()))
        for i in range(k):
            a[a.index(max(a))] = 0
        print(max(a))

main()
