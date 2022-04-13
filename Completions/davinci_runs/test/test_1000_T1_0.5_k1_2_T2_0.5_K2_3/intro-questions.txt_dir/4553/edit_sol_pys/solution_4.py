

import re

def main():
    S = input()
    if re.match(r'^[a-z]{0,3}\d{2,8}[A-Z]{3,}$', S):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
