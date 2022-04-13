

import sys

def main():
    keywords = list()
    for line in sys.stdin.readlines()[1:]:
        keywords.append(line.replace('-', ' ').lower().strip().replace(' ', '-'))
    keywords = set(keywords)
    print(len(keywords))

if __name__ == '__main__':
    main()
