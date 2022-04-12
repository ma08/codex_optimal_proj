

import sys
import math

def get_nearest_char(char):
    if char in ['b', 'c', 'd', 'g', 'k', 'n', 'p', 't']:
        return char
    elif char in ['a', 'e', 'i', 'o', 'u']:
        return 'a'
    elif char in ['f', 'h', 'j', 'l', 'm', 'q', 'r', 'v', 'w', 'x', 'y', 'z']:
        return 'b'
    elif char in ['B', 'C', 'D', 'G', 'K', 'N', 'P', 'T']:
        return char
    elif char in ['A', 'E', 'I', 'O', 'U']:
        return 'A'
    elif char in ['F', 'H', 'J', 'L', 'M', 'Q', 'R', 'V', 'W', 'X', 'Y', 'Z']:
        return 'B'

def get_nearest_ending(char):
    if char in ['b', 'c', 'd', 'g', 'k', 'n', 'p', 't']:
        return 'ah'
    elif char in ['B', 'C', 'D', 'G', 'K', 'N', 'P', 'T']:
        return 'AH'
    elif char in ['a', 'e', 'i', 'o', 'u']:
        return 'uh'
    elif char in ['A', 'E', 'I', 'O', 'U']:
        return 'UH'
    elif char in ['f', 'h', 'j', 'l', 'm', 'q', 'r', 'v', 'w', 'x', 'y', 'z']:
        return 'oh'
    elif char in ['F', 'H', 'J', 'L', 'M', 'Q', 'R', 'V', 'W', 'X', 'Y', 'Z']:
        return 'OH'

def solve(sentence):
    words = sentence.split(' ')
    for i in range(len(words)):
        word = words[i]
        if word == 'Each':
            word = 'Each'
        else:
            if word[0] != '-':
                word = get_nearest_char(word[0])
            for j in range(1, len(word)):
                if word[j] in ['b', 'c', 'd', 'g', 'k', 'n', 'p', 't', 'B', 'C', 'D', 'G', 'K', 'N', 'P', 'T']:
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
