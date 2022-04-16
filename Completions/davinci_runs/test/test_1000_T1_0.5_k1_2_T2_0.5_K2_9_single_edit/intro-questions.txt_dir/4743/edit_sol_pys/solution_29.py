
import sys
import math

def main():
    # Get input and split into words
    sentence = sys.stdin.read().strip().split()

    # Translate
    translated = []
    for word in sentence:
        translated.append(translate(word))

    # Print translation
    print(' '.join(translated))

def translate(word):
    # Split word into syllables
    syllables = word.split('-')

    # Translate each syllable
    for i in range(len(syllables)):
        syllables[i] = translate_syllable(syllables[i])

    return ''.join(syllables)

def translate_syllable(syllable):
    # First letter of syllable
    if syllable[0] in 'acegikmoqsuwy':
        if syllable[0] < 'n':
        # Replace with b if < n, p if >= n
            syllable = syllable.replace(syllable[0], 'b', 1)
        else:
            syllable = syllable.replace(syllable[0], 'p', 1)

    # Special case for 'each'
    if syllable == 'each':
        syllable = 'dach'

    # Subsequent consonants of syllable
    if len(syllable) > 1:
        for i in range(1, len(syllable)):
            # Replace with first consonant
            if syllable[i] in 'bcdfghjklmnpqrstvwxz':
                syllable = syllable.replace(syllable[i], syllable[0], 1)


    # Last letter of syllable
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
