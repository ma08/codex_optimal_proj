
import os
import sys

def main():
    try:
        words = sys.stdin.readline().strip().split()
        phrase = set()
        for word in words:
            if word in phrase:
                print('no')
                return
            phrase.add(word)
        print('yes')
    except:
        print('no')

if __name__ == '__main__':
    main()
