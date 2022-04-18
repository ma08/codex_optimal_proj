

import sys

def main():
    words = sys.stdin.readline().strip().split()
    phrase = set()
    for word in words:
        if word in phrase:
            print('no')
            return
        phrase.add(word)
    print('yes')

if __name__ == '__main__':
    main()