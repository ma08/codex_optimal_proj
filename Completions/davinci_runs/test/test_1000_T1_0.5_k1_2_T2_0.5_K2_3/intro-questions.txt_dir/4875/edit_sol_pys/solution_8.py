
import sys

def pig_latin(word):
    if word[0] in 'aeiouAEIOU':
        return word + 'ay'
    else:
        for i in range(len(word)):
            if word[i] in 'aeiouAEIOU':
                return word[i:] + word[:i] + 'ay'

def main():
    for line in sys.stdin:
        line = line.strip().split(' ')
        for i in range(len(line)):
            line[i] = pig_latin(line[i])
        print(' '.join(line) + '\n')

if __name__ == '__main__':
    main()
