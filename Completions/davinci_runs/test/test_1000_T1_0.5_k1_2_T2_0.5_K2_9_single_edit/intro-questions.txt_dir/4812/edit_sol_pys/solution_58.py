
import sys

def get_input(file=None):
    if file is None:
        f = sys.stdin
    else:
        f = open(file)

    word = f.readline().strip()
    num_endings = int(f.readline())
    endings = [set(f.readline().strip().split()) for _ in range(num_endings)]
    num_phrases = int(f.readline())
    phrases = [f.readline().strip() for _ in range(num_phrases)]

    return word, endings, phrases

def main(file=None):
    word, endings, phrases = get_input(file)

    for phrase in phrases:
        last_word = phrase.split()[-1]
        if any(last_word.endswith(ending) for ending in endings):
            print('YES')
        else:
            print('NO')

if __name__ == '__main__':
    main('/home/codio/workspace/public/py/rhyming_slang.txt')
