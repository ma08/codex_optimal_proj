
import sys

def main():
    keywords = []
    for line in sys.stdin.readlines()[1:]:
        keywords.append(line.replace('-', ' ').lower().strip())
    keywords = set(keywords)
    print(len(keywords))

if __name__ == '__main__':
    main()
