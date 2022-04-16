

from sys import stdin

def main():
    n = int(stdin.readline())
    names = []
    for _ in range(n):
        names.append(stdin.readline())
    names = sorted(names)
    if names == sorted(names, reverse=True):
        print('DECREASING')
    elif names == sorted(names):
        print('INCREASING')
    else:
        print('NEITHER')

main()
