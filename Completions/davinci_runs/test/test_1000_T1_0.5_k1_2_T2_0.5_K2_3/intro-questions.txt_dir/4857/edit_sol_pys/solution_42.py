
import sys
import string

def main():
    lines = sys.stdin.readlines()
    L, W = map(int, lines[0].split())

    if W > L * 26:
        print('impossible')
        return

    letters = string.ascii_lowercase
    weights = range(1, 27)
    letter_dict = dict(zip(letters, weights))

    for letter in letters:
        if W - letter_dict[letter] > 0:
            print(letter, end='')
            W -= letter_dict[letter]
            L -= 1
        else:
            break

    while L > 0:
        print('a', end='')
        L -= 1

    print()

if __name__ == '__main__':
    main()
