
from sys import stdin

def main():
    n = int(stdin.readline().strip())
    names = []
    for _ in range(n):
        names.append(stdin.readline().strip())
    if names == sorted(names, reverse=True): #decreasing
        print('DECREASING')
    elif names == sorted(names): #increasing
        print('INCREASING')
    else:
        print('NEITHER')

main()
