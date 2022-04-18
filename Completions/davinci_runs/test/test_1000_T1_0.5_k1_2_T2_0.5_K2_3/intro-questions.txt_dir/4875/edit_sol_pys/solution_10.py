
import sys

def pig_latin(word):
    if word[0] in 'aeiou':
        return word + 'ay'
    for i in range(len(word)):
        if word[i] in 'aeiou':
            return word[i:] + word[:i] + 'ay'

def main():
    for line in sys.stdin:
        line = line.strip().split(' ')
        for i in range(len(line)):
            line[i] = pig_latin(line[i])
        print(' '.join(line))

if __name__ == '__main__':
    main()
