
import sys

def pig_latin(word):
    if word[0] in 'aeiouAEIOU':
        return word + 'yay'
    else:
        for i in range(len(word)):
            if word[i] in 'aeiouAEIOU':
                return word[i:] + word[:i] + 'ay'

def main():
    for line in sys.stdin:
        print(' '.join([pig_latin(word) for word in line.strip().split()]))

if __name__ == '__main__':
    main()
