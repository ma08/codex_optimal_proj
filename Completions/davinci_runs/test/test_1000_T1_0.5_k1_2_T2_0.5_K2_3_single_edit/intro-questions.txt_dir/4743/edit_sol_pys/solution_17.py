
import sys

def main():
    # Get input
    sentence = sys.stdin.readline().strip()

    # Translate each word
    translated = ''
    for i in range(len(sentence)):
        translated += translate(sentence[i])

    # Print
    print(translated)

def translate(word):
    # Get syllables
    syllables = []
    syllable = ''
    for i in range(len(word)):
        if word[i] == '-':
            syllables.append(syllable)
            syllable = ''
        else:
            syllable += word[i]
    syllables.append(syllable)

    # Translate
    for i in range(len(syllables)):
        syllables[i] = translate_syllable(syllables[i])

    return ''.join(syllables)

def translate_syllable(syllable):
    # First letter - vowels
    if syllable[0] in 'aeiou':
        syllable = 'b' + syllable[1:]

    # First letter - consonants
    elif syllable[0] in 'bcdfghjklmnpqrstvwxz':
        if syllable[0] < 'n':
            syllable = 'b' + syllable[1:]
        elif syllable[0] < 't':
            syllable = 'p' + syllable[1:]
        else:
            syllable = 't' + syllable[1:]

    # Subsequent consonants
    if len(syllable) > 2:
        for i in range(1, len(syllable)):
            if syllable[i] < 'n':
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
