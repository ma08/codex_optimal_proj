
import sys

def pig_latin(word, vowel_set):
    for i in range(len(word)):
        if word[i] in vowel_set:
            return word[i:] + word[:i] + 'ay'

    vowel_set = set('aeiouy')
def main():
    for line in sys.stdin:
        print(' '.join([pig_latin(word, vowel_set) for word in line.split()]))

if __name__ == '__main__':
    main()
