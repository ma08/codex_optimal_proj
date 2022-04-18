

import sys

def main():
    num_cases = int(sys.stdin.readline().strip('\n'))
    for i in range(num_cases):
        n = int(sys.stdin.readline().strip('\n'))
        shuffle = sys.stdin.readline().strip('\n')

        if shuffle == 'out':
            print(n//2)
        else:
            print(n-1)

if __name__ == '__main__':
    main()
