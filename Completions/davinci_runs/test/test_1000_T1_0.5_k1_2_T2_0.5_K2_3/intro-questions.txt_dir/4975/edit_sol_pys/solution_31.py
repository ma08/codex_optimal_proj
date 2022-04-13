
import sys

def playfair(key, plaintext):
    key = key.replace(' ', '').replace('j', '')
    key = ''.join(sorted(set(key), key=key.index)) + ''.join(sorted(set('abcdefghiklmnoprstuvwxyz') - set(key)))
    key = [key[i:i+5] for i in range(0, len(key), 5)] # convert key to 5x5 matrix
    plaintext = plaintext.replace(' ', '').replace('j', 'i')
    if len(plaintext) % 2 == 1:
        plaintext += 'x'
    plaintext = [plaintext[i:i+2] for i in range(0, len(plaintext), 2)] # convert plaintext to digraphs
    ciphertext = ''
    for digraph in plaintext:
        if digraph[0] == digraph[1]:
            digraph = digraph[0] + 'x' + digraph[1]
        for row in key:
            if digraph[0] in row and digraph[1] in row:
                if row.index(digraph[0]) < row.index(digraph[1]):
                    ciphertext += row[row.index(digraph[0])+1] + row[row.index(digraph[1])+1]
                else:
                    ciphertext += row[row.index(digraph[0])-1] + row[row.index(digraph[1])-1]
            elif digraph[0] in row or digraph[1] in row:
                if digraph[0] in row:
                    ciphertext += row[row.index(digraph[0])] + key[(key.index(row)+1)%5][row.index(digraph[0])]
                else:
                    ciphertext += row[row.index(digraph[1])] + key[(key.index(row)+1)%5][row.index(digraph[1])]
    return ciphertext.upper()

def main():
    key = sys.stdin.readline().strip()
    plaintext = sys.stdin.readline().strip()
    print(playfair(key, plaintext))

if __name__ == '__main__':
    main()
