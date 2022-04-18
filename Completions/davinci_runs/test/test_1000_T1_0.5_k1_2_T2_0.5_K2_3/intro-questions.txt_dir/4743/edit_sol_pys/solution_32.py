
import sys

def main():
    # Get input
    sentence = sys.stdin.readline().strip().split()

    # Translate
    translated = []
    for word in sentence:
        translated.append(translate(word))

    # Print
    print(' '.join(translated))

def translate(word):
    # Get syllables
    syllables = word.split('-')

    # Translate
    for i in range(len(syllables)):
        syllables[i] = translate_syllable(syllables[i])

    return ''.join(syllables)

def translate_syllable(syllable):
    # First letter, if consonant
    if syllable[0] in 'bcdfghjklmnpqrstvwxz':
        if syllable[0] < 'n':
            syllable = syllable.replace(syllable[0], 'b', 1)
        elif syllable[0] < 't':
            syllable = syllable.replace(syllable[0], 'p', 1)
        else:
            syllable = syllable.replace(syllable[0], 'f', 1)

    # If syllable is "each" or "etch"
    if syllable == 'each' or syllable == 'etch':
        syllable = 'dach'

    # Subsequent consonants, if any
    if len(syllable) > 1:
        for i in range(1, len(syllable)):
            if syllable[i] in 'bcdfghjklmnpqrstvwxz':
                syllable = syllable.replace(syllable[i], syllable[0], 1)

    # End consonant, if any
    if syllable[-1] in 'bcdfghjklmnpqrstvwxz':
        if syllable[-1] < 'n':
            syllable += 'ah'
        elif syllable[-1] < 't':
            syllable += 'oh'
        else:
            syllable += 'uh'

    return syllable

if __name__ == '__main__':
    main()
