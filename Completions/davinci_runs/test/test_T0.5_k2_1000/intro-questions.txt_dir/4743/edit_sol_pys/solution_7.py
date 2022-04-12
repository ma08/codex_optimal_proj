
import sys
import math

def main():
    sentence = sys.stdin.readline().strip()

    # Translate sentence
    translated = translate(sentence)

    # Print sentence
    print(' '.join(translated))

def translate(word):
    # Split sentence into words
    words = word.split()

    # Translate words
    for i in range(len(words)):
        words[i] = translate_word(words[i])

    return ' '.join(words)

def translate_word(word):
    # Split word into syllables
    syllables = word.split('-')

    # Translate syllables
    for i in range(len(syllables)):
        syllables[i] = translate_syllable(syllables[i])

    return ''.join(syllables)

def translate_syllable(syllable, end=False):
    # First letter (consonant)
    if syllable[0] in 'acegikmoqsuwy' and not end:
        syllable = syllable.replace(syllable[0], 'b' if syllable[0] < 'n' else 'p', 1)

    # Each (consonant)
    if syllable == 'each':
        syllable = 'dach'

    # Subsequent consonants (vowel)
    if len(syllable) > 1:
        for i in range(len(syllable)):
            if syllable[i] in 'bcdfghjklmnpqrstvwxz' and not end:
                syllable = syllable.replace(syllable[i], 'ah' if syllable[i] < 'n' else 'oh' if syllable[i] < 't' else 'uh', 1)

    # End consonant (vowel)
    if syllable[-1] in 'bcdfghjklmnpqrstvwxz' and not end:
        syllable += 'ah' if syllable[-1] < 'n' else 'oh' if syllable[-1] < 't' else 'uh'

    return syllable

if __name__ == '__main__':
    main()
