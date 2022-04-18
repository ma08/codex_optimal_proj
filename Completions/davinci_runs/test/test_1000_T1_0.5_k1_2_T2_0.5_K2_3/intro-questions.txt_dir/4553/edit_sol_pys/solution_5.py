

import re

def main():
    A, B = map(int, input().split())
    S = input()
    if re.match(rf'\d{{A}}-\d{{B}}', S):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
