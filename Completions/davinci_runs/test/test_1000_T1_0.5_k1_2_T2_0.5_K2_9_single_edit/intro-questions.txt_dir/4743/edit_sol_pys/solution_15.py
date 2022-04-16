
import sys
import math

def main():
    # get input
    sentence = sys.stdin.readline().strip().split()

    # translate
    translated = []
    for word in sentence:
        translated.append(translate(word))

    # print
    print(' '.join(translated))

def translate(word):
    # get syllables
    syllables = word.split('-')

    # translate
    for i in range(len(syllables)):
        syllables[i] = translate_syllable(syllables[i])

    return ''.join(syllables)

def translate_syllable(syllable):
    # first letter
    if syllable[0] in 'acegikmoqsuwy':
        if syllable[0] < 'n':
            syllable = syllable.replace(syllable[0], 'b', 1)
        else:
            syllable = syllable.replace(syllable[0], 'p', 1)

    # each
    if syllable == 'each':
        syllable = 'dach'

    # subsequent consonants
    if len(syllable) > 1:
        for i in range(1, len(syllable)):
            if syllable[i] in 'bcdfghjklmnpqrstvwxz':
                syllable = syllable.replace(syllable[i], syllable[0], 1)

    # end consonant
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
