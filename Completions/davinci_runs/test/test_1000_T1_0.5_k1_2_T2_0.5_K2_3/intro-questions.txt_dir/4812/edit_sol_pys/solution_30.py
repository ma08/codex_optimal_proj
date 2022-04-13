
import sys

def get_input(file=None):
    if file is None:
        f = sys.stdin
    else:
        f = open(file)

    word = f.readline().strip()
    num_endings = int(f.readline().strip())
    endings = [f.readline().strip() for _ in range(num_endings)] # TODO: what if they are the same?
    num_phrases = int(f.readline().strip())
    phrases = [f.readline().strip() for _ in range(num_phrases)] # TODO: what if they are the same?

    return word, endings, phrases

def main(file=None):
    word, endings, phrases = get_input(file)

    for phrase in phrases:
        last_word = phrase.split()[-1] # TODO: what if there are no words?
        if any(last_word.endswith(ending) for ending in endings): # TODO: what if the word is shorter than the ending?
            print('YES')
        else:
            print('NO')

if __name__ == '__main__':
    main('rhyming_slang.txt')
