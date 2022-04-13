
from sys import stdin

def main():
    n = int(stdin.readline().strip())
    names = []
    for _ in range(n):
        names.append(stdin.readline().strip())
    names1 = sorted(names)
    names2 = sorted(names, reverse=True)
    if names == names2:
        print('DECREASING')
    elif names == names1:
        print('INCREASING')
    else:
        print('NEITHER')

main()
