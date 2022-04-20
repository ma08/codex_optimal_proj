


def shift_alphabet(word, shift):
    alphabet = [chr(i) for i in range(65, 91)]
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    shifted_word = ''
    for letter in word:
        shifted_word += shifted_alphabet[alphabet.index(letter)]
    return shifted_word


def main():
    shift = int(input())
    word = input()
    print(shift_alphabet(word, shift))


if __name__ == '__main__':
    main()