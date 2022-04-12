
import re
import sys

def main():
    for line in sys.stdin:
        line = line.strip()
        line = re.sub(r'[^a-zA-Z]', '', line)
        print(line.lower())

if __name__ == '__main__':
    main()
