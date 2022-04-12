
import sys

def playfair(key, plaintext):
    key = key.replace(" ", "")
    key = "".join(sorted(set(key), key=key.index))
    key += "".join(sorted(set("abcdefghiklmnopqrstuvwxyz") - set(key)))
    key = key.replace("j", "")
    key = [key[i : i + 5] for i in range(0, len(key), 5)]
    plaintext = plaintext.replace(" ", "")
    plaintext = plaintext.replace("j", "i")
    plaintext = [plaintext[i : i + 2] for i in range(0, len(plaintext), 2)]
    ciphertext = ""
    for digraph in plaintext:  # iterate through digraphs
        if digraph[0] == digraph[1]:  # if same letter
            digraph = digraph[0] + "x" + digraph[1]
        for row in key:  # iterate through rows
            if digraph[0] in row and digraph[1] in row:  # if both letters in same row
                if row.index(digraph[0]) < row.index(digraph[1]):  # if first letter is to the left of second letter
                    ciphertext += row[row.index(digraph[0]) + 1] + row[row.index(digraph[1]) + 1]
                else:
                    ciphertext += row[row.index(digraph[0]) - 1] + row[row.index(digraph[1]) - 1]
            elif digraph[0] in row or digraph[1] in row:  # if only one letter in row
                if digraph[0] in row:  # if first letter in row
                    ciphertext += row[row.index(digraph[0])] + key[(key.index(row) + 1) % 5][row.index(digraph[0])]
                else:
                    ciphertext += row[row.index(digraph[1])] + key[(key.index(row) + 1) % 5][row.index(digraph[1])]
    return ciphertext.upper()

def main():
    key = sys.stdin.readline().strip()
    plaintext = sys.stdin.readline().strip()
    print(playfair(key, plaintext))

if __name__ == '__main__':
    main()
