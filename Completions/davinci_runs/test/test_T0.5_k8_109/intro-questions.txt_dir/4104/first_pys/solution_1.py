

import re

def main():
    input = raw_input()
    print(re.sub(r'(\d+)', r'0\1', input))

if __name__ == '__main__':
    main()