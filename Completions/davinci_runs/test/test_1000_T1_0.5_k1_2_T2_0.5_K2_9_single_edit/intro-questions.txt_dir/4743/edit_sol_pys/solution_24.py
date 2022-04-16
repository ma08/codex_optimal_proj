

import sys
import math

def get_nearest_char(char):
    if char in ['b', 'c', 'd', 'g', 'k', 'n', 'p', 't', 'B', 'C', 'D', 'G', 'K', 'N', 'P', 'T']:
        return char
    elif char in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
        return 'a'
    elif char in ['f', 'h', 'j', 'l', 'm', 'q', 'r', 'v', 'w', 'x', 'y', 'z', 'F', 'H', 'J', 'L', 'M', 'Q', 'R', 'V', 'W', 'X', 'Y', 'Z']:
        return 'b'

def get_nearest_ending(char):
    if char in ['b', 'c', 'd', 'g', 'k', 'n', 'p', 't', 'B', 'C', 'D', 'G', 'K', 'N', 'P', 'T']:
        return 'ah'
    elif char in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
        return 'uh'
    elif char in ['f', 'h', 'j', 'l', 'm', 'q', 'r', 'v', 'w', 'x', 'y', 'z', 'F', 'H', 'J', 'L', 'M', 'Q', 'R', 'V', 'W', 'X', 'Y', 'Z']:
        return 'oh'

def solve(sentence):
    words = sentence.split(' ')
    for i in range(len(words)):
        word = words[i]
        if word == 'Each':
            word = 'Dach'
        else:
            if word[0] != '-':
                word = get_nearest_char(word[0])
            for j in range(1, len(word)):
                if word[j] in ['b', 'c', 'd', 'g', 'k', 'n', 'p', 't']:
                    word = word[:j] + word[0] + word[j+1:]
            if word[-1] not in ['a', 'e', 'i', 'o', 'u']:
                word += get_nearest_ending(word[-1])
        words[i] = word
    return ' '.join(words)

def main():
    sentence = sys.stdin.readline().strip()
    print(solve(sentence))

if __name__ == '__main__':
    main()
