
import sys

def get_input(file=None):
    if file is None:
        f = sys.stdin
    else:
        f = open(file)

    word = f.readline().strip()
    num_endings = int(f.readline())  # number of endings, 1 <= num_endings <= 100
    endings = [set(f.readline().strip().split()) for _ in range(num_endings)]  # endings, 1 <= len(endings) <= 100
    num_phrases = int(f.readline())
    phrases = [f.readline().strip() for _ in range(num_phrases)]  # phrases, 1 <= len(phrases) <= 100

    return word, endings, phrases

def main(file=None):
    word, endings, phrases = get_input(file)

    for phrase in phrases:
        last_word = phrase.split()[-1]
        if any(last_word.endswith(ending) for ending in endings):  # check if last word ends with any of the endings
            print('YES')
        else:
            print('NO')

if __name__ == '__main__':
    main('rhyming_slang.txt')
