import sys


def input():
    return sys.stdin.readline().strip()

def main():
    n = int(input())
    names = []
    for _ in range(n):
        names.append(input())
    names = sorted(names)
    if names == sorted(names, reverse=True):
        print('DECREASING')
    elif names == sorted(names):
        print('INCREASING')
    else:
        print('NEITHER')

main()
