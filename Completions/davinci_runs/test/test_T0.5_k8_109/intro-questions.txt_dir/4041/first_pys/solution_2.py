

import sys
import re

def main():
    s = sys.stdin.readline().strip()
    t = sys.stdin.readline().strip()
    print(len(s) - len(re.sub(f'[^{t}]', '', s)))

if __name__ == '__main__':
    main()