
import sys


    """
    Reads a sentence from stdin, decodes it, and prints it to stdout.
    """
def main():
    sentence = sys.stdin.readline().strip()
    word = ''
    decoded_sentence = ''

    for letter in sentence:
        if letter == ' ':
            if word != '':
                decoded_sentence += word + ' '
                word = ''
        else:
            if letter == 'p' or letter == 'P':
                word += letter
            else:
                word += letter + 'P' + letter

    if word != '':
        decoded_sentence += word


    print(decoded_sentence)

if __name__ == '__main__':
    main()
