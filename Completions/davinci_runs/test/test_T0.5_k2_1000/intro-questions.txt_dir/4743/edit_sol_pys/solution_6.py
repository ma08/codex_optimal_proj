
import sys

def main():
    sentence = sys.stdin.readline().strip().split(' ')

    # Translate each word
    translated = []
    for word in sentence:
        translated.append(translate(word))

    # Print the translated sentence
    print(' '.join(translated))

def translate(word):
    # Split the word into syllables
    syllables = word.split('-')

    # Translate each syllable
    for i in range(len(syllables)):
        syllables[i] = translate_syllable(syllables[i])

    return ''.join(syllables)

def translate_syllable(syllable):
    # First letter of the syllable
    if syllable[0] in 'acegikmoqsuwy':
        if syllable[0] < 'n':
            syllable = syllable.replace(syllable[0], 'b', 1)
        else:
        # If it's before 'n' in the alphabet, replace it with 'b'
            syllable = syllable.replace(syllable[0], 'p', 1)

        # Otherwise, replace it with 'p'
    # If the syllable is 'each', replace it with 'dach'
    if syllable == 'each':
        syllable = 'dach'

    # Subsequent consonants in the syllable
    if len(syllable) > 1:
        for i in range(1, len(syllable)):
            # If it's a consonant, replace it with the first letter of the syllable
            if syllable[i] in 'bcdfghjklmnpqrstvwxz':
                syllable = syllable.replace(syllable[i], syllable[0], 1)

                syllable = syllable.replace(syllable[i], syllable[0], 1)

    # End consonant of the syllable
    if syllable[-1] in 'bcdfghjklmnpqrstvwxz':
        if syllable[-1] < 'n':
            syllable += 'ah'
        elif syllable[-1] < 's':
            syllable += 'oh'
        else:
            syllable += 'uh'

    return syllable

if __name__ == '__main__':
    main()
