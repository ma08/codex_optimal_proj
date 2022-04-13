

# SOLUTION 2

import sys

def main():
    n = int(sys.stdin.readline())
    dutch_words = sys.stdin.readline().split()
    m = int(sys.stdin.readline())
    translations = {}
    for i in range(m):
        dutch_word, english_word, correctness = sys.stdin.readline().split()
        if dutch_word not in translations:
            translations[dutch_word] = []
        translations[dutch_word].append((english_word, correctness))

    correct, incorrect = translate(dutch_words, translations)
    print(correct, 'correct')
    print(incorrect, 'incorrect')

def translate(dutch_words, translations):
    if len(dutch_words) == 0:
        return 1, 0
    word = dutch_words[0]
    translation_options = translations[word]
    correct = 0
    incorrect = 0
    for translation, correctness in translation_options:
        rest = dutch_words[1:]
        if correctness == 'correct':
            correct += translate(rest, translations)[0]
        else:
            incorrect += translate(rest, translations)[1]
    return correct, incorrect

if __name__ == '__main__':
    main()
