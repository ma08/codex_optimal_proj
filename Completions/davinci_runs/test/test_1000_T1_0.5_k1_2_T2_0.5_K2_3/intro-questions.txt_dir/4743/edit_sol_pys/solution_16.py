
import sys
import math

def main():
    # Getting input
    sentence = sys.stdin.readline().strip().split()

    # Translating
    translated = []
    for word in sentence:
        translated.append(translate(word))

    # Printing
    print(' '.join(translated))

def translate(word):
    # Getting syllables
    syllables = word.split('-')

    # Translating
    for i in range(len(syllables)):
        syllables[i] = translate_syllable(syllables[i])

    return ''.join(syllables)

def translate_syllable(syllable):
    # First letter of word
    if syllable[0] in 'acegikmoqsuwy':
        if syllable[0] < 'n':
            syllable = syllable.replace(syllable[0], 'b', 1)
        else:
            syllable = syllable.replace(syllable[0], 'p', 1)

    # Each word
    if syllable == 'each':
        syllable = 'dach'

    # Subsequent consonants of word
    if len(syllable) > 1:
        for i in range(1, len(syllable)):
            if syllable[i] in 'bcdfghjklmnpqrstvwxz':
                syllable = syllable.replace(syllable[i], syllable[0], 1)

    # End consonant of word
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
