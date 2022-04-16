

import sys
import re
vowels = ['a','e','i','o','u']

def pig_latin(word):
    if re.match('[aeiouy]', word[0]):
        return word + 'yay' #add yay if word starts with a vowel
    for i in range(len(word)): #find first vowel
        if re.match('[aeiouy]', word[i]):
            break #break when first vowel is found
    return word[i:] + word[:i] + 'ay' #move first group of consonants to end of word and add ay

def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    lines = []
    for line in sys.stdin:
        lines.append(line.strip())

    for line in lines:
        words = line.split()
        for i in range(len(words)):
            words[i] = pig_latin(words[i])
        print(' '.join(words))

if __name__ == "__main__":
    main('pig')
