

import re

def main():
    S = input()
    if re.match(r'\d{3}-\d{4}', S):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
