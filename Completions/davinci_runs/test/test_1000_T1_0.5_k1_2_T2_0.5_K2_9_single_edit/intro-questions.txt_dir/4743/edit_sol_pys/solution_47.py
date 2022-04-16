
import sys
import math

def main():
    sentence = sys.stdin.readline().strip()

    print(translate(sentence))

def translate(word):
    # Remove punctuation
    word = word.strip('.?!')

    # Get syllables
    syllables = word.split('-')[::-1]

    # Translate
    for i in range(len(syllables) - 1):
        syllables[i] = translate_syllable(syllables[i])

    return ''.join(syllables[::-1])

def translate_syllable(syllable):
    # First letter
    if syllable[0] in 'acegikmoqsuwy':
        if syllable[0] < 'n':
            syllable = syllable.replace(syllable[0], 'b', 1)
        else:
            syllable = syllable.replace(syllable[0], 'p', 1)

    # Each
    if syllable == 'each' or syllable == 'etch':
        syllable = 'eetch'

    # Subsequent consonants
    if len(syllable) > 1:
        for i in range(1, len(syllable)):
            if syllable[i] in 'bcdfghjklmnpqrstvwxz':
                syllable = syllable.replace(syllable[i], syllable[0], 1)

    # End consonant
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
