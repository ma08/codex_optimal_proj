

import sys
import string

def main():
    lines = sys.stdin.readlines()
    l, w = map(int, lines[0].split())

    if w > l * 26 or w < l or w == 0:
        print('impossible')
        return

    letters = string.ascii_lowercase
    weights = range(1, 27)
    letter_dict = dict(zip(letters, weights))

    for letter in letters:
        if w - letter_dict[letter] > 0:
            print(letter, end='')
            w -= letter_dict[letter]
            l -= 1
        else:
            break

    while l > 0:
        print('a', end='')
        l -= 1

    print()

if __name__ == '__main__':
    main()
