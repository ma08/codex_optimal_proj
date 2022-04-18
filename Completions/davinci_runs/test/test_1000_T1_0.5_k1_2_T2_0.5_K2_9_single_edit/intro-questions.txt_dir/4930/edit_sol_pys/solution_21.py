

import sys

def main():
    sentence = sys.stdin.readline().strip().lower()
    word = ''
    decoded_sentence = ''

    for letter in sentence:
        if letter == ' ':
            if word != '':
                decoded_sentence += word + ' '
                word = ''
        else:
            if letter == 'p':
                word += letter
            else:
                word += letter + 'p' + letter

    if word != '':
        decoded_sentence += word

    print(decoded_sentence)

if __name__ == '__main__':
    main()
