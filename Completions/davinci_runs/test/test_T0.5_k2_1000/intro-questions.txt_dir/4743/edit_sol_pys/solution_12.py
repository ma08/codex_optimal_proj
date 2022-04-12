
import sys

def main():
    lines = sys.stdin.readlines()
    output = []
    for line in lines:
        output.append(nimion(line.strip()))

    print('\n'.join(output))

def nimion(word):
    syllables = word.split('-')
    output = []
    for syllable in syllables:
        output.append(nimion_syllable(syllable))

    return ''.join(output)

def nimion_syllable(syllable):
    if syllable == 'Each':
        return 'Dach' # 'Dach' is the correct spelling
    elif syllable.startswith('h'):
        return syllable[1].lower() + syllable[2:] # 'h' is silent
    else:
        return syllable[0].lower() + syllable[1:]

if __name__ == '__main__':
    main()
