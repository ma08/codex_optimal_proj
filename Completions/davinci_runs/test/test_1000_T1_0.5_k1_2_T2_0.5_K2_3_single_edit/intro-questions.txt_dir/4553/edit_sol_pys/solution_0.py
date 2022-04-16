

import re

def main():
    s = input()
    if re.match(r'\d{3}-\d{4}', s):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
