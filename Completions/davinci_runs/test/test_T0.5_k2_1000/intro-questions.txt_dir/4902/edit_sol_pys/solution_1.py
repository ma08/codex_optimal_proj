

import sys

def main():
    word = sys.stdin.readline().strip()
    counter = {}
    for letter in word:
        if letter not in counter:
            counter[letter] = 0
        counter[letter] += 1
    odd = 0
    for value in counter.values():
        if value % 2 != 0:
            odd += 1
    if odd == 0:
        print(0)
    else:
        print(odd - 1)

if __name__ == '__main__':
    main()
