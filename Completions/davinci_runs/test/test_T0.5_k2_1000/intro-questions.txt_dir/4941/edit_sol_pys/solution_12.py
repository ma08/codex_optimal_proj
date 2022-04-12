

# SOLUTION 1


import sys

def main():
    n = int(sys.stdin.readline())
    dutch = sys.stdin.readline().split()
    m = int(sys.stdin.readline())
    dictionary = {}
    for i in range(m):
        dutch_word, english_word, correctness = sys.stdin.readline().split()
        if dutch_word not in dictionary:
            dictionary[dutch_word] = []
        dictionary[dutch_word].append((english_word, correctness))

    correct, incorrect = translate(dutch, dictionary)
    print(correct, 'correct')
    print(incorrect, 'incorrect')


def translate(dutch, dictionary):
    if len(dutch) == 0:
        return 1, 0
    word = dutch[0]
    translations = dictionary[word]
    correct = 0
    incorrect = 0
    for translation, correctness in translations:
        rest = dutch[1:]
        if correctness == 'correct':
            correct += translate(rest, dictionary)[0]
        else:
            incorrect += translate(rest, dictionary)[1]
    return correct, incorrect


if __name__ == '__main__':
    main()
