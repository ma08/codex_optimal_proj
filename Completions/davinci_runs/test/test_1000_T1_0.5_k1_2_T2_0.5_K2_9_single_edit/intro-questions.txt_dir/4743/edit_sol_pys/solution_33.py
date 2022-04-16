
import sys
import string
import math

def main():
    while True:
        line = sys.stdin.readline().strip()
        words = line.split(' ')
        output = []
        for word in words:
            output.append(nimion(word))

        print(' '.join(output))

def nimion(word):
    syllables = word.split('-')
    output = []
    for syllable in syllables:
        if len(syllable) > 0:
            output.append(nimion_syllable(syllable))

    return ''.join(output)

def nimion_syllable(syllable):
    if syllable == 'Each' or syllable == 'each':
        return 'Dach'
    elif syllable.startswith('h') or syllable.startswith('H'):
        return syllable[1].lower() + syllable[2:]
    elif syllable[0] in string.punctuation:
        return syllable[0] + syllable[1].lower() + syllable[2:]
    elif syllable[0] in string.digits:
        return syllable[0] + syllable[1].lower() + syllable[2:]
    else:
        return syllable[0].lower() + syllable[1:]

if __name__ == '__main__':
    main()
