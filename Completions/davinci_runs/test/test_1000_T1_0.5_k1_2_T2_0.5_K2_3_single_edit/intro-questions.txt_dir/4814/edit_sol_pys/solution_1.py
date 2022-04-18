

from sys import stdin

def main():
    n = int(stdin.readline().strip())
    names = []
    for _ in range(n):
        names.append(stdin.readline().strip())
    sorted_names = sorted(names)
    if sorted_names == sorted(names, reverse=True):
        print('DECREASING')
    elif sorted_names == sorted(names):
        print('INCREASING')
    else:
        print('NEITHER')

main()
