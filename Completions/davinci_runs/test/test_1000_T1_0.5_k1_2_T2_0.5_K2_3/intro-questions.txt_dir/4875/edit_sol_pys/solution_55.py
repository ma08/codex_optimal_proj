
import sys

def pig_latin(word1):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if word1[0] in vowels:
        return word1 + 'ay'
    elif word1[0] not in vowels:
        for j in range(len(word1)):
            if word1[j] in vowels:
                return word1[j:] + word1[:j] + 'ay'

def main():
    for line in sys.stdin:
        print(' '.join([pig_latin(word) for word in line.split()]))

if __name__ == '__main__':
    main()
