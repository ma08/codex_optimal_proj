
import sys

def main():
    line = sys.stdin.readline()
    words = line.strip().split(' ')
    output = []
    for word in words:
        output.append(nimion(word))

    print(' '.join(output).lower())

def nimion(word):
    syllables = word.split('-')
    output = []
    for syllable in syllables:
        output.append(nimion_syllable(syllable))

    return ''.join(output)

def nimion_syllable(syllable):
    if syllable == 'Each' or syllable == 'Earch' or syllable == 'Eath':
        return 'Dach'
    elif syllable.startswith('h'):
        return syllable[1:]
    else:
        return syllable[0] + syllable[1:]

if __name__ == '__main__':
    main()
