
import sys

def main():
    # Get input and split into words
    sentence = sys.stdin.readline().strip().split(' ')

    # Translate and join
    translated = []
    for word in sentence:
        translated.append(translate_word(word))
    print(' '.join(translated), end='')

def translate(word):
    # Split into syllables
    syllables = word.split('-')

    # Translate each syllable
        # Translate
    for i in range(len(syllables)):
        # Add hyphen
        if i < len(syllables) - 1:
            syllables[i] += '-'
        syllables[i] = translate_syllable(syllables[i])

    return ''.join(syllables)

def translate_syllable(syllable):
    # First letter (vowel)
    if syllable[0] in 'acegikmoqsuwy':
        if syllable[0] <= 'm':
            syllable = syllable.replace(syllable[0], 'b', 1)
        else:
            syllable = syllable.replace(syllable[0], 'p', 1)

    # Each (special case)
    if syllable == 'each':
        syllable = 'dach'

    # Subsequent consonants (consonant)
    if len(syllable) > 1:
        for i in range(1, len(syllable)):
            if syllable[i] in 'bcdfghjklmnpqrstvwxz':
                syllable = syllable.replace(syllable[i], syllable[0], 1)

    # End consonant (consonant)
    if syllable[-1] in 'bcdfghjklmnpqrstvwxz':
        if syllable[-1] <= 'm':
            syllable += 'ah'
        elif syllable[-1] <= 'r':
            syllable += 'oh'
        else:
            syllable += 'uh'

    return syllable

if __name__ == '__main__':
    main()
