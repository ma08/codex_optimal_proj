
import re
import sys

def main():
    sentence = sys.stdin.readline()
    print(re.sub(r'p(.)(.*)\1', r'\1\2\1', sentence))

    for letter in sentence:
        if letter == ' ':
            if word != '':
                decoded_sentence.append(word)
                word = ''
        else:
            if letter == 'p':
                word += letter
            else:
                word += letter + 'p' + letter

    if word != '':
        decoded_sentence.append(word)

    print(' '.join(decoded_sentence))

if __name__ == '__main__':
    main()
