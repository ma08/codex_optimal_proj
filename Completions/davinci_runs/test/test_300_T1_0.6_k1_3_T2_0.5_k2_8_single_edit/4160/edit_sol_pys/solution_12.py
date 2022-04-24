

import sys
import re

def main():
    s = sys.stdin.readline()
    s = re.sub(r'[^a-zA-Z]', '', s)
    s = s.lower()

    print(s)
    print(len(s))

if __name__ == '__main__':
    main()
