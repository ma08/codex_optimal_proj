import sys
import math

def encrypt(phrase, key):
    # remove spaces in phrase
    phrase = phrase.replace(' ', '')
    # if the phrase is odd, add an 'x' to the end of it
    if len(phrase) % 2 != 0:
        phrase += 'x'
    # split phrase into pairs
    pairs = [phrase[i:i+2] for i in range(0, len(phrase), 2)]
    # encrypt each pair
    encrypted_pairs = []
    for pair in pairs:
        # if the pair contains two equal letters, add an 'x' after the first letter
        if pair[0] == pair[1]:
            pair = pair[0] + 'x' + pair[1]
        # get the positions of the letters in the key
        letter1_pos = [i for i, x in enumerate(key) if x == pair[0]][0]
        letter2_pos = [i for i, x in enumerate(key) if x == pair[1]][0]
        # get the row and column of the first letter
        letter1_row = int(math.floor(letter1_pos / 5))
        letter1_col = letter1_pos % 5
        # get the row and column of the second letter
        letter2_row = int(math.floor(letter2_pos / 5))
        letter2_col = letter2_pos % 5
        # if the letters are in the same row, replace them with the letters to their immediate right respectively
        if letter1_row == letter2_row:
            letter1_col = (letter1_col + 1) % 5
            letter2_col = (letter2_col + 1) % 5
        # if the letters are in the same column, replace them with the letters immediately below respectively
        elif letter1_col == letter2_col:
            letter1_row = (letter1_row + 1) % 5
            letter2_row = (letter2_row + 1) % 5
        # if the letters are not in the same row or column, replace them with the letters on the same row respectively but at the other pair of corners of the rectangle defined by the original pair
        else:
            letter1_col, letter2_col = letter2_col, letter1_col
        # get the positions of the new letters in the key
        letter1_pos = letter1_row * 5 + letter1_col
        letter2_pos = letter2_row * 5 + letter2_col
        # get the new letters
        letter1 = key[letter1_pos]
        letter2 = key[letter2_pos]
        # add the new pair to the list of encrypted pairs
        encrypted_pairs.append(letter1 + letter2)
    # join the encrypted pairs and return the encrypted phrase
    encrypted_phrase = ''.join(encrypted_pairs)
    return encrypted_phrase

def main(filepath):
    # read the file
    with open(filepath, 'r') as f:
        lines = f.read().splitlines()
    # get the key phrase and phrase to encrypt
    key_phrase = lines[0]
    phrase = lines[1]
    # remove spaces and duplicate letters in the key phrase
    key_phrase = ''.join(sorted(set(key_phrase.replace(' ', '')), key=key_phrase.index))
    # fill the table with the key phrase
    table = []
    for i in range(0, len(key_phrase), 5):
        table.append(list(key_phrase[i:i+5]))
    # fill the rest of the table with the rest of the letters of the alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet = alphabet.replace('q', '')
    for letter in alphabet:
        if letter not in key_phrase:
            for row in table:
                if len(row) < 5:
                    row.append(letter)
                    break
    # flatten the table
    table = [letter for row in table for letter in row]
    # encrypt the phrase
    encrypted_phrase = encrypt(phrase, table)
    # print the encrypted phrase
    print(encrypted_phrase)

if __name__ == '__main__':
    main(sys.argv[1])
