import sys
import string

def main():
    lines = sys.stdin.readlines()
    l, w = map(int, lines[0].split()) # l = length of string, w = weight

    if w > l * 25: # if weight is too much for length
        print('impossible')
        return

    letters = string.ascii_lowercase
    weights = list(range(1, 26))
    letter_dict = dict(zip(letters, weights))

    for letter in letters: # if weight is not too much, fill the string with letters
        if w - letter_dict[letter] >= 0:
            print(letter, end='')
            w -= letter_dict[letter]
            l -= 1
        else:
            break

    while l > 0: # fill the rest of the string with 'a'
        print('a', end='')
        l -= 1

    print()

if __name__ == '__main__':
    main()
