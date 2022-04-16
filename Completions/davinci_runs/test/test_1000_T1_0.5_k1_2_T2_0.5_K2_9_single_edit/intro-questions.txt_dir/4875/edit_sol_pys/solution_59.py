
import sys

def pig_latin(word):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    if word[0] in vowels:
        return word + "yay" #returns word if it starts with a vowel
    else:
        for i in range(len(word)):
            if word[i] in vowels:
                return word[i:] + word[:i] + "ay" #returns word if it starts with a consonant

def main():
    for line in sys.stdin:
        words = line.split()
        for word in words:
            print(pig_latin(word), end=" ")
        print()

if __name__ == "__main__":
    main()
