from sys import stdin

def main():
    n = int(stdin.readline().strip())
    names = []
    for _ in range(n):
        names.append(stdin.readline().strip())
    if names == sorted(names) and names == sorted(names, reverse=True):
        print('NEITHER')
    elif names == sorted(names):
        print('INCREASING')
    else:
        print('DECREASING')

main()
