

from sys import stdin

def main():
    n = int(stdin.readline().strip())
    names = [stdin.readline().strip() for _ in range(n)]
    if names == sorted(names, reverse=True): #sort names in reverse
        print('DECREASING ORDER')
    elif names == sorted(names): #sort names in order
        print('INCREASING ORDER')
    else: #neither
        print('NEITHER')

main()
