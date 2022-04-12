from sys import stdin

def read():
    return stdin.readline()

def main():
    n, m = (int(x) for x in read().split())
    a = [int(x) for x in read().split()]
    a.sort()
    print(a)

main()
