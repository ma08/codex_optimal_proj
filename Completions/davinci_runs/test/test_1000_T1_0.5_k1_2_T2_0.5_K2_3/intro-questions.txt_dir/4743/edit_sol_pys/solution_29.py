

import sys

def main():
    for line in sys.stdin:
        words = line.strip().split(' ')
        output = []
        for word in words:
            output.append(nimion(word))
        print(' '.join(output))
    return ''.join(nimion_syllables(word))

def nimion(word):
    return ''.join(nimion_syllables(word))

def nimion_syllable(syllable):
    if syllable == 'Each':
        return 'Dach' # and not 'Datch'
    elif syllable.startswith('h'):
        return syllable[1].lower() + syllable[2:]
    else:
        return syllable[0].lower() + syllable[1:]

def nimion_syllables(word):
    syllables = word.split('-')
    output = []
    for syllable in syllables:
        output.append(nimion_syllable(syllable))
    return output

if __name__ == '__main__':
    main()
