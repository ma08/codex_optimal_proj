import sys

def main():
    n = int(input())
    d = [int(x) for x in input().split()]
    d.append(0)
    d.append(n-1)
    d.sort()
    for i in range(n):
        print(d.index(i)+1,end=' ')


main()
