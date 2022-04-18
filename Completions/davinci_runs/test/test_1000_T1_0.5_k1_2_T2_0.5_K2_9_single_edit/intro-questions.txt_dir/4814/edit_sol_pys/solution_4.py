

from sys import stdin

def main():
    n = int(stdin.readline().strip())
    names = []
    for _ in range(n):
        names.append(stdin.readline().strip())
    names = sorted(names)
    if names == sorted(names, reverse=True):
        print('DECREASING')
    elif names == sorted(names):
        print('INCREASING')
    else:
        print('NEITHER')
