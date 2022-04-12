import re

import sys

def main():
    keywords = list()
    for line in sys.stdin.readlines()[1:]:
        line = re.sub(r'[^\w\s]', ' ', line)
        keywords.append(line.lower().strip())
    keywords = set(keywords)
    print(len(keywords))

if __name__ == '__main__':
    main()
