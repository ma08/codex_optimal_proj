

import sys
import math

def nimionese(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = ['b', 'c', 'd', 'g', 'k', 'n', 'p', 't']
    nimionese_word = ''
    
    # Replace the first letter with the nearest hard consonant
    if word[0] in consonants:
        nimionese_word += word[0]
    else:
        if word[0] in vowels:
            nimionese_word += 'b'
        else:
            nimionese_word += chr(ord(word[0]) - 1)
    
    for i in range(1, len(word)):
        if word[i] in consonants:
            if word[i] == 'h':
                word = word[:i] + word[i+1:]
            elif word[i] == 'p':
                word = word[:i] + 'b' + word[i+1:]
            elif word[i] == 't':
                word = word[:i] + 'd' + word[i+1:]
            elif word[i] == 'g':
                word = word[:i] + 'c' + word[i+1:]
        elif word[i] == 'e':
            word = word[:i] + 'dach' + word[i+1:]
    word = word.replace('-', '')
    nimionese_word += word[1:]
    
    # Add the ending
    if word[-1] not in consonants:
        nimionese_word += 'ah'
    else:
        if word[-1] == 'n':
            nimionese_word += 'ah'
        elif word[-1] == 'k':
            nimionese_word += 'oh'
        else:
            nimionese_word += 'uh'
    
    return nimionese_word

def main():
    sentence = sys.stdin.readline().strip()
    words = sentence.split(' ')
    
    nimionese_sentence = ''
    
    for word in words:
        nimionese_sentence += nimionese(word) + ' '
    
    print(nimionese_sentence[:-1])
    
if __name__ == '__main__':
    main()