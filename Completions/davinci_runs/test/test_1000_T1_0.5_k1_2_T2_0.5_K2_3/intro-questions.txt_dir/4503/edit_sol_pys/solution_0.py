

import sys

def main():
    N, A, B = map(int, input().split())
    if N <= A: 
        print('Yes')
    elif N % (A + B) <= A and N % (A + B) != 0:
        print('Yes')
    elif N % (A + B) == 0:
        print('No')

if __name__ == '__main__':
    main()
