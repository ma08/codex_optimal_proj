"""
    File: file.py
    Author: Kevin Falconett
    Purpose: encrypts a message using the vigenere cipher
"""

def shift(c, key, i):
    if i % 2 == 0:
        return chr((ord(c) - ord('A') + ord(key[i]) - ord('A')) % 26 + ord('A'))
    else:
        return chr((ord(c) - ord('A') - (ord(key[i]) - ord('A'))) % 26 + ord('A'))

def main():
    """
        main function that gets inputs from user and prints the encrypted message
    """
    c = input()
    k = input()
    print("".join(shift(c[i], k, i) for i in range(len(c))))

if __name__ == "__main__":
    main()
