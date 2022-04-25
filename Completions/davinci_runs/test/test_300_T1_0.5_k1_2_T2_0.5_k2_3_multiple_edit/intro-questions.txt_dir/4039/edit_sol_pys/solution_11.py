
import sys
import re

def fix_spelling(dictionary, misspelled_word):
    return dictionary.get(misspelled_word)


def main():
    if len(sys.argv) < 3:
        print('Usage: python spellcheck.py <dictionary> <file>')
        sys.exit(1)

    dictionary_file = sys.argv[1]
    text_file = sys.argv[2]

    dictionary = {}
    with open(dictionary_file) as file:
        for line in file:
            line = line.strip()
            dictionary[line] = line
    
    with open(text_file) as file:
        for line in file:
            line = line.strip()
            words = re.split(r'[^a-zA-Z]', line)
            for word in words:
                word = word.lower()
                if word in dictionary:
                    continue
                else:
                    print(word)
                    replacement = fix_spelling(dictionary, word)
                    if replacement:
                        print(f'\t{replacement}')
                    else:
                        print('\t(unknown)')


if __name__ == "__main__":
    main()
