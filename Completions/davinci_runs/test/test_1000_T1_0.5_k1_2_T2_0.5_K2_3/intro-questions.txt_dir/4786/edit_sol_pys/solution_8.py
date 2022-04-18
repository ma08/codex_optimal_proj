
# python3
import sys

def main():
    keywords = list()
    for line in sys.stdin.readlines():
        keywords.append(line.replace('-', ' ').lower().strip())
    keywords = set(keywords)
    print(len(keywords))

if __name__ == '__main__':
    main()
