
import sys
import math

def main():
    for line in sys.stdin:
        line = line.strip()
        words = line.split(' ')
        output = []
        for word in words:
            output.append(nimion(word))

        print(' '.join(output))

def nimion(word):
    syllables = word.split('-')
    output = []
    for syllable in syllables:
        output.append(nimion_syllable(syllable))

    return ''.join(output)

def nimion_syllable(syllable):
    if syllable == 'Each':
        return 'Dach'
    elif syllable.startswith('h'):
        return syllable[1].lower() + syllable[2:]
    else:
        return syllable[0].lower() + syllable[1:]

if __name__ == '__main__':
    main()
