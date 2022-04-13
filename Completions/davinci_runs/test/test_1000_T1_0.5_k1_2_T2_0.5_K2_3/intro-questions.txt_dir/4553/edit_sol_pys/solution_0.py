

import re

def main():
    S = input()
    print('Yes' if re.match(r'\d{3}-\d{4}', S) else 'No')

if __name__ == '__main__':
    main()
