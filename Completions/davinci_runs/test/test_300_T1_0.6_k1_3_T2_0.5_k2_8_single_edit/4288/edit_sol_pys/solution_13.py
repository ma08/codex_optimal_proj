
import sys

def main():
    triple = [int(x) for x in sys.stdin.readline().split()]
    if triple[0] == triple[1] and triple[1] != triple[2]:
        print('Yes')
    elif triple[0] == triple[2] and triple[2] != triple[1]:
        print('Yes')
    elif triple[1] == triple[2] and triple[2] != triple[0]:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
