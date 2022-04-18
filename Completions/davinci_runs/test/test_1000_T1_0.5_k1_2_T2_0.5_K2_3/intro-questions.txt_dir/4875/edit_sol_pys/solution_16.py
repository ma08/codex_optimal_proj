
import re
import sys

def pig_latin(word):
    if re.match(r'[aeiou]', word):
        return word + 'yay' #yay is added to the end of the word
    else:
        for i in range(len(word)): #iterates through the word
            if re.match(r'[aeiou]', word[i]): #checks if the letter is a vowel
                return word[i:] + word[:i] + 'ay' #ay is added to the end of the word, the vowels are moved to the end, and the consonants are moved to the front

def main():
    for line in sys.stdin:
        line = line.strip().split(' ')
        for i in range(len(line)):
            line[i] = pig_latin(line[i])
        print(' '.join(line))

if __name__ == '__main__':
    main()
