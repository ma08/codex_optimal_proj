import sys

def main():
    sentence = input().strip()
    word = ''
    decoded_sentence = []

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
