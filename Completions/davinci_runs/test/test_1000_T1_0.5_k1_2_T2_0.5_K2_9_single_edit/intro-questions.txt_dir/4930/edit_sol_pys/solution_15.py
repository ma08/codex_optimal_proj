
import sys

def main():
    sentence = sys.stdin.readline()
    word = ''
    encoded_sentence = ''

    for letter in sentence:
        if letter == ' ':
            if word != '':
                encoded_sentence += word + ' '
                word = ''
        else:
            if letter == 'p':
                word += letter
            else:
                word += letter + 'p' + letter

    if word != '':
        encoded_sentence += word

    print(encoded_sentence)

if __name__ == '__main__':
    main()
