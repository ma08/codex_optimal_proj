

import sys

if __name__ == '__main__':
    N, K = map(int, input().strip().split())
    if K >= N:
        print('Your wish is granted!')
    else:
        print('You will become a flying monkey!') 
