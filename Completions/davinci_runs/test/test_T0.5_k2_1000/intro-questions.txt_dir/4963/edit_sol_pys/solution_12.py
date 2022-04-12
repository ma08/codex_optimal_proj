

import sys

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    a.append(0)
    a.append(n)
    a = sorted(a)
    for i in range(n):
        print(a.index(i)+1,end=' ')


main()
