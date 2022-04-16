

#SOLUTION

import sys

def main():
    n = int(sys.stdin.readline())
    dutch = sys.stdin.readline().split()
    m = int(sys.stdin.readline())
    dict = {}
    for i in range(m):
        dutch_word, english_word, correctness = sys.stdin.readline().split()
        if dutch_word not in dict:
            dict[dutch_word] = []
        dict[dutch_word].append((english_word, correctness))

    print(translate(dutch, dict))


def translate(dutch, dict):
    if len(dutch) == 0:
        return 1
    word = dutch[0]
    translations = dict[word]
    result = 0
    for translation, correctness in translations:
        rest = dutch[1:]
        result += translate(rest, dict)
    return result


if __name__ == '__main__':
    main()
